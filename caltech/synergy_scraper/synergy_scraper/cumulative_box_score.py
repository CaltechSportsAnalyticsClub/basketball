import pandas as pd

class CumulativeBoxScore:
    def __init__(self, filename):
        self.filename = filename
    def df(self):
        df = pd.read_html(self.filename)[0]
        df["USG%"] = df["Poss"]/(df["Poss"].sum()/2) * 100
        df["PPG"] = df["Pts"] / df["GP"]
        df["RPG"] = df["Tot Reb"] / df["GP"]
        df["Off RPG"] = df["Off Reb"] / df["GP"]
        df["Def RPG"] = df["Def Reb"] / df["GP"]
        df["APG"] = df["Ast"] / df["GP"]
        df["SPG"] = df["Stl"] / df["GP"]
        df["BPG"] = df["Blk"] / df["GP"]
        df["TOVPG"] = df["TO"] / df["GP"]
        df["FTA PG"] = df["FT Att"] / df["GP"]
        df["FTM PG"] = df["FT Made"] / df["GP"]
        df["FGA PG"] = df["FG Att"] / df["GP"]
        df["FGM PG"] = df["FG Made"] / df["GP"]
        df["3PA PG"] = df["3FG Att"] / df["GP"]
        df["3PM PG"] = df["3 FG Made"] / df["GP"]
        df["Ast Per 100 Poss"] = df["Ast"] / df["Poss"] * 100
        df["Stl Per 100 Poss"] = df["Stl"] / df["Poss"] * 100
        df["Blk Per 100 Poss"] = df["Blk"] / df["Poss"] * 100
        df["Reb Per 100 Poss"] = df["Tot Reb"] / df["Poss"] * 100
        df["Off Reb Per 100 Poss"] = df["Off Reb"] / df["Poss"] * 100
        df["Def Reb Per 100 Poss"] = df["Def Reb"] / df["Poss"] * 100
        return df