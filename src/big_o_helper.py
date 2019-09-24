import json
import os
import glob

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

            data_dict[test_length] = test_mean_time

def get_big_o(data_dict):
    pass


get_big_o('bubble')
