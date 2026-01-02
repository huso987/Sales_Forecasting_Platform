import pandas as pd

class DataService:
    def load(self, path="data/Kaynak_Dosya.txt"):
        return pd.read_csv(path, sep=";")
