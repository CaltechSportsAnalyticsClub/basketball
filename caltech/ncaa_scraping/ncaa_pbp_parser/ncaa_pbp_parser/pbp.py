import pandas as pd
import requests as r
import re
import numpy as np

class PlayByPlay:
  def __init__(self, game_id=None):
    assert game_id is not None, "Game ID must be provided"
    self.game_id = game_id
    self.did_scrape = False
  
  def _pbp_link(self):
    return f'https://data.ncaa.com/casablanca/game/{self.game_id}/pbp.json'
  
  def _get_base_df(self):
    try:
        pbp = r.get(self._pbp_link()).json()
        self.pbp_df = pd.DataFrame([y for x in [p['playStats'] for p in pbp['periods']] for y in x])
    except:
        raise ValueError("Request failed: Invalid game id")
  
  def _fill_in_cum_stats(self):
    self.pbp_df['homeRebounds'] = self.pbp_df['homeText'].str.contains(' REBOUND ', case=False).cumsum()
    self.pbp_df['visitorRebounds'] = self.pbp_df['visitorText'].str.contains(' REBOUND ', case=False).cumsum()
    self.pbp_df['homeBlocks'] = self.pbp_df['homeText'].str.contains(' Block ', case=False).cumsum()
    self.pbp_df['visitorBlocks'] = self.pbp_df['visitorText'].str.contains(' Block ', case=False).cumsum()
    self.pbp_df['homeSteals'] = self.pbp_df['homeText'].str.contains(' Steal ', case=False).cumsum()
    self.pbp_df['visitorSteals'] = self.pbp_df['visitorText'].str.contains(' Steal ', case=False).cumsum()
  
  def _find_possessions(self, time, home, vis):
    homeOut, visOut = np.zeros((len(home), 1), dtype=np.int32), np.zeros((len(home), 1), dtype=np.int32)
    # this technique misses the first possession
    for i in range(len(home)):
        # set vars for which team is focus of this event
        desc = home[i].lower()
        curr = home
        currOut = homeOut
        otherOut = visOut
        if home[i] == "":
            desc = vis[i].lower()
            curr = vis
            currOut = visOut
            otherOut = homeOut

        # two types of things. either possession ends so for other team possession started
        # spaces around "good" bc what if someone's name is good or smths
        if " good " in desc and "free throw" not in desc:
            otherOut[i+1] = 1 # made a free throw we litty
        elif "defensive rebound " in desc:
            currOut[i] = 1 # this team got possession in that event
        elif "turnover" in desc:
            otherOut[i] = 1 # other team got possession in that event
        elif "free throw good " in desc: 
            # check events after of same timestamp that they are not free throw
            j = i+1
            last = True
            while j < len(time) and time[i] == time[j]:
                if "free throw good " in curr[j].lower():
                    last = False
                    j = len(time)
                j += 1
            if last:
                inc = 1
    return homeOut, visOut
  
  def _fill_in_possessions(self):
    self.pbp_df['homePossessions'], self.pbp_df['visitorPossessions'] = self._find_possessions(self.pbp_df['time'].to_numpy(), self.pbp_df['homeText'].to_numpy(), self.pbp_df['visitorText'].to_numpy())
    self.pbp_df['homePossessions'] = self.pbp_df['homePossessions'].cumsum()
    self.pbp_df['visitorPossessions'] = self.pbp_df['visitorPossessions'].cumsum()
  
  def _fill_in_score(self):
    self.pbp_df['score'] = self.pbp_df['score'].mask(self.pbp_df['score'] == "")
    self.pbp_df['score'] = self.pbp_df['score'].bfill()
    self.pbp_df['score'] = self.pbp_df['score'].ffill() 
  
  def scrape(self):
    self._get_base_df()
    self._fill_in_score()
    self._fill_in_cum_stats()
    self._fill_in_possessions()
    self.did_scrape = True

a = PlayByPlay(game_id=6060646)
a.scrape()
print(a.pbp_df)