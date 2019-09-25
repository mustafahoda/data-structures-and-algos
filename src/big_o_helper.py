import json
import os
import glob

import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error as mse

from pdb import set_trace

cwd = os.getcwd()

def get_length(test_name):

    ctr = 0
    index = 0

    for _ in test_name:
        if _ == '_':
            ctr = ctr + 1

        if ctr == 3: break

        index = index + 1

    return test_name[index + 1:]


def populate_dict(algo):
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

    p1 = np.poly1d(np.polyfit(x, y, 1))
    p2 = np.poly1d(np.polyfit(x,y,2))

    y1 = p1(x)
    y2 = p2(x)

    plt.scatter(x, y, color = 'g')
    plt.plot(x, y1, color = 'r')
    plt.plot(x, y2, color = 'b')

    set_trace()

    mse1 = mse(y1, y)
    mse2 = mse(y2, y)

data_dict = populate_dict('bubble')
# set_trace()
get_big_o(data_dict)