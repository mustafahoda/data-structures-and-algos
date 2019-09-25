import json
import os
import glob

import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error as mse

cwd = os.getcwd()

def get_length(test_name):
    '''
    returns the length of the list the test was ran upon
    '''

    ctr = 0
    index = 0

    for _ in test_name:
        if _ == '_':
            ctr = ctr + 1

        if ctr == 3: break

        index = index + 1

    return test_name[index + 1:]


def populate_data_dict(algo):

    '''
    Populates a dictionary data_dict with the length of the list as the key and the mean of it's sorting as the value
    :param algo: selection, quick, bubble, merge
    :return:

    {
        1: 0.000123,
        5: 0.0034234890,
        10: 0.0004981237467856430
    }

    '''
    list_of_files = glob.glob(cwd + '/test/results/' + algo + '_sort_*[0-15000]*.json')

    data_dict = {} # dictionary used to store input size the time it took to sort that list

    for file in list_of_files:
        with open(file) as json_data:
            data = json.load(json_data)
            test_length = get_length(data['benchmarks'][0]['name'])
            test_mean_time = data['benchmarks'][0]['stats']['mean']

            data_dict[int(test_length)] = test_mean_time

    return data_dict

def get_big_o(data_dict):

    x = np.array(list(data_dict.keys()))
    y = np.array(list(data_dict.values()))

    # Create a polynomial for O(n) and O(n^2)
    O_n = np.poly1d(np.polyfit(x, y, 1))
    O_n_2 = np.poly1d(np.polyfit(x, y, 2))

    y_O_n = O_n(x)
    y_O_n_2 = O_n_2(x)

    plt.scatter(x, y, color = 'g')
    plt.scatter(x, y_O_n, color = 'r')
    plt.scatter(x, y_O_n_2, color = 'b')
    plt.show()

    big_O_dict = {
        mse(y_O_n, y) : 'O(n)',
        mse(y_O_n_2, y) : 'O(n^2)'
    }

    min_lookup = min(big_O_dict.keys())

    return big_O_dict[min_lookup]
