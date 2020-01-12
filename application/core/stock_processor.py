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
        self.dataset = self.dataset.sort_index(ascending=True, axis=0)
        self.dataset = self.dataset.iloc[:, 3:7].replace({'\$': ''}, regex=True).astype(float)
        # data_normalizer = MinMaxScaler()
        # self.dataset = data_normalizer.fit_transform(self.dataset)

        # print(self.dataset.high)
        # plt.figure(figsize=(32,8))
        # plt.plot(self.dataset.high.values)
        # plt.show()

    def show_dataset(self):
        print(self.dataset)

    # the average between low and high values of the specified date
    # then the average of the column 
    def estimate_stock_average(self, date):
        subset = self.dataset.loc[date]

        return str(subset.loc[:, ('low', 'high')].mean(axis=1).mean())

    def predict_stock(self, date):
        self.preprocess_stock()
        new_set = pd.DataFrame(columns=['avg'])
        new_set['avg'] = self.dataset.loc[:, ('low', 'high')].mean(axis=1)

        # creating train and test sets
        ds = new_set.values
        train = ds[0:700, :]
        valid = ds[700:, :]
        
        # converting dataset into x_train and y_train
        scaler = MinMaxScaler(feature_range=(0, 1))
        scaled_data = scaler.fit_transform(ds)

        x_train, y_train = [], []
        for i in range(60,len(train)):
            x_train.append(scaled_data[i-60: i,0])
            y_train.append(scaled_data[i, 0])
        x_train, y_train = np.array(x_train), np.array(y_train)

        x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
        
        # create and fit the LSTM network
        model = Sequential()
        model.add(LSTM(units=50, return_sequences=True, input_shape=(x_train.shape[1], 1)))
        model.add(LSTM(units=50))
        model.add(Dense(1))

        model.compile(loss='mean_squared_error', optimizer='adam')
        model.fit(x_train, y_train, epochs=1, batch_size=1, verbose=2)

        # predicting
        inputs = new_set[len(new_set) - len(valid) - 60:].values
        inputs = inputs.reshape(-1, 1)
        inputs  = scaler.transform(inputs)
        
        X_test = []
        for i in range(60, inputs.shape[0]):
            X_test.append(inputs[i-60:i,0])
        X_test = np.array(X_test)

        X_test = np.reshape(X_test, (X_test.shape[0],X_test.shape[1],1))
        avg_price = model.predict(X_test)
        avg_price = scaler.inverse_transform(avg_price)

        #plot
        train = new_set[:700]
        valid = new_set[700:]
        valid['predictions'] = avg_price

        print(valid)
        
        plt.figure(figsize=(32,8))
        plt.plot(train.values)
        plt.plot(valid.values)
        plt.show()


if __name__ == "__main__":
    sp = StockProcessor('dow_jones_index.data')
    # sp.preprocess_stock()
    sp.predict_stock('2011-01-28')