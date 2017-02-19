__author__ = 'Zeynab'
import numpy as np
import pandas
from sklearn.preprocessing import MinMaxScaler
from biosppy.signals.tools import smoother

#set params
look_back = 500
horizon = 5
min_range = -50
max_range = 50
total_length = 60000


def read_sample(path, name):
    try:
        #print('1')
        #signal = np.loadtxt(path+name+'.txt', skiprows=5)
        dataset = pandas.read_csv(path + name + '.txt', delimiter='\t', skiprows=4)
    except:
        print('Error in reading file!')
    #print('2')
    dataset = pandas.read_csv(path + name + '.txt', delimiter='\t', skiprows=4)

    x_signal = dataset.values[:, 0]
    y = dataset.values[:, 1]
    y_signal = normalize_data(pandas.DataFrame(y), max_range, min_range)
    #smoothed_signal,params = smoother(y_signal)
    dataset =dataset.as_matrix()
    return dataset, x_signal, y_signal


#Normalize data in specified range
def normalize_data(dataset, max=max_range, min=min_range):
    scaler = MinMaxScaler(feature_range=(min, max))
    data = scaler.fit_transform(dataset)
    #move to fit baseline to zero
    index = np.where(dataset == 0)
    value = data[index[0][0]]
    data = data-value
    return data