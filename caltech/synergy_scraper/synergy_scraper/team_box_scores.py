import os
import pandas as pd

class TeamBoxScore:
  def __init__(self, team_folder, opponent_folder):
    self.team_folder = team_folder
    self.opponent_folder = opponent_folder
    self.team_df = pd.DataFrame()
    self.opponent_df = pd.DataFrame()

  def team_box_scores(self):
    team_box_scores = []
    for filename in os.listdir(self.team_folder):
      f = os.path.join(self.team_folder, filename)
      html = pd.read_html(f)
      starters = html[0].iloc[-1]
      bench = html[1].iloc[-1]
      df_add = starters.add(bench, fill_value=0)
      self.team_df = pd.concat([self.team_df, df_add], axis=1)
    return team_box_scores