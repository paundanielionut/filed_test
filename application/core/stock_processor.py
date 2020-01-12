import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import numpy as np
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense, Dropout, LSTM

pd.plotting.register_matplotlib_converters()
# figure size
from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 20,10

class StockProcessor(object):
    def __init__(self, stock_file):
        super().__init__()
        self.stock_file = stock_file

        self.dataset = pd.read_csv(self.stock_file)
        
        # self.X = self.dataset.iloc[:, [2, 4, 5]]
        # self.y = self.dataset.iloc[:, 1]
        
    def preprocess_stock(self):
        self.dataset['date'] = pd.to_datetime(self.dataset.date, format='%m/%d/%Y')
        self.dataset.index = self.dataset['date']

        self.dataset = self.dataset.iloc[:, 3:7].replace({'\$': ''}, regex=True).astype(float)
        # data_normalizer = MinMaxScaler()
        # self.dataset = data_normalizer.fit_transform(self.dataset)

        # plt.figure(figsize=(16,8))
        # plt.plot(self.dataset['close'].values, label='Close Price')
        # plt.show()

    def show_dataset(self):
        print(self.dataset)

    # the average between low and high values of the specified date
    # then the average of the column 
    def estimate_stock_average(self, date):
        subset = self.dataset.loc[date]

        return str(subset.loc[:, ('low', 'high')].mean(axis=1).mean())

    def predict_stock(self, date):
        pass


if __name__ == "__main__":
    sp = StockProcessor('dow_jones_index.data')
    sp.preprocess_stock()
    print((sp.estimate_stock('2011-01-28')))