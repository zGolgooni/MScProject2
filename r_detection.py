__author__ = 'Zeynab'
from biosppy.signals import ecg
import numpy as np
import plotly.plotly as py
import plotly.graph_objs as go
from plotly import tools


#    temp_rpeaks = ecg.engzee_segmenter(signal=signal[:, 1], sampling_rate=rate)
def detect_r_points(signal, length, rate, algorithm='none'):
    length = signal.shape[0]
    ecg_out = ecg.ecg(signal=signal[:,0], sampling_rate=rate, show=False)
    filtered = ecg_out.__getitem__('filtered')
    temp_rpeaks = ecg_out.__getitem__('rpeaks')
    #engzee_out = ecg.engzee_segmenter(signal=filtered, sampling_rate=rate)
    #temp_rpeaks = engzee_out.__getitem__('rpeaks')
    #try:
    rpeaks = np.empty([temp_rpeaks.shape[0], 1], dtype=int)
    for i,r in enumerate(temp_rpeaks):
        #find maximum
        rpeaks[i] = r
        max_best_so_far = r
        end = False
        #while not end:
            #end = True
        for j in range(25):
            neighbor1 = max_best_so_far - j
            neighbor2 = max_best_so_far + j
            if abs(signal[neighbor1]) > abs(signal[max_best_so_far]):
                max_best_so_far = neighbor1
                    #end = False
            if abs(signal[neighbor2]) > abs(signal[max_best_so_far]):
                max_best_so_far = neighbor2
                    #end = False
        rpeaks[i] = max_best_so_far
    print('finished finalizing r points! :)')

    #except:
     #   print('Biosppy error (Not enough beats to compute heart rate :?)')
    return rpeaks


def plot_rpoint_result(signal, rpeaks, name, length=20000):
    #plot result of r detection
    trace1 = go.Scatter(y=signal[:20000,1], x=signal[:20000,0], name='Signal')
    trace2 = go.Scatter(y=signal[rpeaks, 1], x=signal[rpeaks,0],mode='markers', name='final R peaks')
    layout = go.Layout(title=name)
    figure = go.Figure(data=[trace1, trace2], layout=layout)
    py.plot(figure, filename='biosppy test of r peaks detection')
    print('Plotting is done! :)')


'''
def detect_r_points(signal, length, rate, algorithm='none'):
    length = signal.shape[0]
    out = ecg.ecg(signal=signal[:, 1], sampling_rate=rate, show=False)
    try:
        if algorithm == 'christov_segmenter':
            temp_rpeaks = ecg.christov_segmenter(signal, rate)
        elif algorithm == 'hamilton_segmenter':
            temp_rpeaks = ecg.hamilton_segmenter(signal, rate)
        elif algorithm == 'engzee_segmenter':
            temp_rpeaks = ecg.engzee_segmenter(signal, rate)
        else:
            temp_rpeaks = out.__getitem__('rpeaks')
    except:
        print('Error in r detection!')

    try:
        rpeaks = np.empty([temp_rpeaks.shape[0], 1], dtype=int)
        for i,r in enumerate(temp_rpeaks):
            #find maximum
            rpeaks[i] = r
            max_best_so_far = r
            end = False
            #while not end:
                #end = True
            for j in range(25):
                neighbor1 = max_best_so_far - j
                neighbor2 = max_best_so_far + j
                if abs(signal[neighbor1, 1]) > abs(signal[max_best_so_far, 1]):
                    max_best_so_far = neighbor1
                    #end = False
                if abs(signal[neighbor2, 1]) > abs(signal[max_best_so_far, 1]):
                    max_best_so_far = neighbor2
                    #end = False
            rpeaks[i] = max_best_so_far
        print('finished finalizing r points! :)')
    except:
        print('Biosppy error (Not enough beats to compute heart rate :?)')
    return rpeaks


'''