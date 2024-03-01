import glob
import os
import pandas as pd

from sentic import SenticPhrase
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from nrclex import NRCLex


class TextAnalyer:
    def __init__(self, dir: str):
        self.dir = dir

    @staticmethod
    def read_txt(path: str) -> str:
        with open(path, "r") as f:
            txt = f.read()

        return txt
    
    @staticmethod
    def run_sentic(txts: dict) -> list:
        data = list()
        for fname in txts:
            content = txts[fname]
            sentics = SenticPhrase(content).get_sentics()

            row = {key: sentics[key] for key in sentics}
            row["file"] = fname
            data.append(row)        

        return data
    
    @staticmethod
    def run_lex(txts: dict) -> list:
        data = list()
        for fname in txts:
            content = txts[fname]
            emotion = NRCLex(content)
            scores = emotion.affect_frequencies

            row = {key: scores[key] for key in scores}
            row["file"] = fname
            data.append(row)

        return data
    
    @staticmethod
    def run_vader(txts: dict) -> dict:
        vader = SentimentIntensityAnalyzer()

        data = list()
        for fname in txts:
            content = txts[fname]
            compound_score = vader.polarity_scores(content)["compound"]

            row = {"file": fname, "polarity": compound_score}
            data.append(row)

        return data   

    def read_dir(self) -> dict:
        p = os.path.join(self.dir, "*.txt")
        file_paths = glob.glob(p)

        data = dict()
        for obj in file_paths:
            fname = obj.split(self.dir)[1]
            contents = self.read_txt(obj)
            data[fname] = contents

        return data
    
    def analyze(self):
        data = self.read_dir()

        lex = pd.DataFrame(self.run_lex(data))
        vader = pd.DataFrame(self.run_vader(data))
        sentics = pd.DataFrame(self.run_sentic(data))

        all_data = lex.merge(vader, how="outer")
        all_data = all_data.merge(sentics, how="outer")
        df = all_data.fillna(0)
        
        save_path = os.path.join(self.dir, "results.csv")
        df.to_csv(save_path, index=False)
