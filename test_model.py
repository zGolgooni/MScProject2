__author__ = 'Zeynab'

from prepare_files import load_file
from prepare_data import read_sample, normalize_data
from simple_classification import classify_by_rpoints
from r_detection import detect_r_points, plot_rpoint_result


def test_file(path, file):
    paths, names, sampling_rates, labels = load_file(path, file)
    tp = 0
    fp = 0
    tn = 0
    fn = 0
    n = 0
    for i in range(len(names)):
        #plot result of r detection
        #plot_rpoint_result(signal, rpeaks, sampling_rates[i])

        #classify
        #predicted_label = test_sample(path + paths[i], names[i], sampling_rates[i], labels[i], plot='False')

        try:
            print('%d' % i)
            predicted_label = test_sample(path + paths[i], names[i], sampling_rates[i], labels[i], plot='False')

            n += 1
            if labels[i] == 'Normal':
                if predicted_label == 'Normal':
                    tp += 1
                else:
                    fn += 1
            else:
                if predicted_label == 'Arrhythmic':
                    tn += 1
                else:
                    fp += 1
        except:
            print('Exception')

    print('\n--->Result for data = %s , %d samples (%d N, %d A)' % (file, n, (fn+tp), (fp+tn)))
    print('\t\ttp = %f, tn = %f, fp = %f, fn = %f, total-> %f\n\n' % (tp, tn, fp, fn, ((tp+tn)/n)))
    return tp, tn, fp, fn, n


def test_sample(path, name, sampling_rate, real_label, plot='False'):
    signal, x_signal, y_signal = read_sample(path, name)
    length = signal.shape[0]
    print('%s-----> %s, sampling rate=%d' % (path+name, real_label, sampling_rate))
    rpeaks = detect_r_points(y_signal, length, sampling_rate)
    print('after r detection!')
    #plot result of r detection
    if plot == 'True':
        plot_rpoint_result(signal, rpeaks, sampling_rate)
    else:
        print('No problem in plot!')

    #classify
    predicted_label, type = classify_by_rpoints(y_signal, rpeaks, sampling_rate)
    print("-> label: real = %s, predicted = %s (%s)\n\n" % (real_label, predicted_label,type))
    return predicted_label