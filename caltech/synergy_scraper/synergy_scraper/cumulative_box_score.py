import pandas as pd

class CumulativeBoxScore:
    def __init__(self, filename):
        self.filename = filename
    def df(self):
        df = pd.read_html(self.filename)[0]
        df["Ast %"] = df["Ast"] / df["Poss"] * 100
        df["Stl %"] = df["Stl"] / df["Poss"] * 100
        df["Blk %"] = df["Blk"] / df["Poss"] * 100
        return df