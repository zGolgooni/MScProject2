__author__ = 'Zeynab'


import numpy as np
import pandas
from scipy.stats import norm
from prepare_files import load_files
from prepare_data import read_sample
from lstm_prepare_data import normalize_data, prepare_for_lstm, min_range, max_range, total_length
from lstm_model import create_model, fit_model, load_model
from rnn_classification import test_file, load_data
from r_detection import detect_r_points
#from biosppy.signals.tools import smoother


main_path = '/Users/Zeynab/PycharmProjects/Msc_project/'
train_files = ['/My data/95.10.21.csv']
#test_files = ['/My data/95.10.15.csv']#,'/My data/before 95.08.csv','/My data/from 95.8.2 till 95.9.17.csv']

#load train data
paths, names, sampling_rates, labels = load_files(main_path, train_files)

mode = 0
if mode == 0:
    #do 1st step
    train_x_reshaped = np.empty([0, 1])
    train_y = np.empty([0, 1])
    counter = 0
    for i in range(len(names)):
        if (labels[i] == 'Normal') & (counter < 5):
            counter += 1
            dataset, x_signal, y_signal = read_sample(paths[i], names[i])
            rpeaks = detect_r_points(y_signal, y_signal.shape[0], sampling_rates[i])

            sample_x, sample_y = load_data(pandas.DataFrame(y_signal), rpeaks, labels[i], 4)
            sample_x_reshaped = np.reshape(sample_x, (sample_x.shape[0], 1, sample_x.shape[1]))
            #sample_y = sample_y[:, :, 0]
            if i == 0:
                train_x_reshaped = sample_x
                train_y = sample_y
            else:
                train_x_reshaped = np.concatenate([train_x_reshaped, sample_x])
                train_y = np.concatenate([train_y, sample_y])
            print("%d ----->%s, %s, sampling rate=%s" % ((i + 1), names[i], labels[i], sampling_rates[i]))

    model = create_model()
    fit_model('1-file21-4000in-50node', model, train_x=train_x_reshaped, train_y=train_y, batch=10000, epoch=50, validation=0.2)
else:
    model = create_model()
    #model = load_model(model,'horizon5-v02.h5')
    model.load_weights('1-file21-4000in-50node.h5')


test_file('/Users/Zeynab/PycharmProjects/Msc_project/','/My data/95.10.21.csv',model=model)
#test_files('/Users/Zeynab/PycharmProjects/Msc_project/','/My data/95.10.15.csv',model=model, normal_mu=normal_mu, normal_std=normal_std, arrhythmic_mu=arrhythmic_mu, arrhythmic_std=arrhythmic_std)

