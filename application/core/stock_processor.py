import pandas as pd
from sklearn import preprocessing
import numpy as np


class StockProcessor(object):
    def __init__(self, stock_file):
        super().__init__()
        self.stock_file = stock_file

        self.dataset = pd.read_csv(self.stock_file)
        
        self.X = self.dataset.iloc[:, :-1]
        self.y = self.dataset.iloc[:, 1]

    def normalize(self):
        data_normalizer = preprocessing.MinMaxScalar()
        self.data_normalized = data_normalizer.fit_transform(self.data)

    def show_dataset(self):
        for row in self.X:
            print(row)