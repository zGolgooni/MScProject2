__author__ = 'Zeynab'
from prepare_data import read_sample, normalize_data
from prepare_files import load_files
from r_detection import detect_r_points, plot_rpoint_result
from simple_classification import classify_by_rpoints
from test_model import test_file
import numpy as np
import plotly.plotly as py
import plotly.graph_objs as go
from plotly import tools

from prepare_files import load_file
from test_model import test_sample

main_path = '/Users/Zeynab/'
file = '/My data/from 95.8.2 till 95.9.17.csv'

files = ['/My data/before 95.08.csv', '/My data/from 95.8.2 till 95.9.17.csv','/My data/95.10.21.csv','/My data/95.10.15.csv']
#test_files = ['/My data/95.10.15.csv']#,'/My data/before 95.08.csv','/My data/from 95.8.2 till 95.9.17.csv']
total_tp = 0
total_tn = 0
total_fp = 0
total_fn = 0
total_n = 0
for file in files:
    tp, tn, fp, fn, n = test_file(main_path, file)
    total_tp += tp
    total_tn += tn
    total_fp += fp
    total_fn += fn
    total_n += n
    print('\t\tTotal results: tp = %f, tn = %f, fp = %f, fn = %f, total-> %f\n\n' % (total_tp, total_tn, total_fp,total_fn,((total_tp+total_tn)/total_n)))



'''
i=29
signal, x_signal, y_signal = read_sample(main_path + paths[i], names[i])
length = signal.shape[0]
rpeaks = detect_r_points(y_signal, length, sampling_rate)
predicted_label, type = classify_by_rpoints(y_signal, rpeaks, sampling_rate)
trace1 = go.Scatter(y=signal[:20000,1], x=signal[:20000,0], name='Signal')
trace2 = go.Scatter(y=signal[rpeaks, 1], x=signal[rpeaks,0],mode='markers', name='final R peaks')
layout = go.Layout(title='from i = 29')
figure = go.Figure(data=[trace1, trace2], layout=layout)
py.plot(figure, filename='biosppy test of r peaks detection')
print('Plotting is done! :)')
'''