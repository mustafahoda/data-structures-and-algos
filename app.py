import ast, os, sys

import click

from src.SortingAlgorithms import sorting_algos


@click.group()
def cli1():
    pass

@cli1.command()
@click.option('--algo', default='quick', help='What type of algorithm would you like to use to sort this list?')
@click.argument('list')
def sort_list(algo, list):
    """A program that sorts using a specified sorting algo"""

    list = ast.literal_eval(list) #Click converst list to String Literal. Converting back to a list

    if algo == 'quick':
        print(sorting_algos.quick_sort(list))
    elif algo == 'bubble':
        print(sorting_algos.bubble_sort(list))
    elif algo == 'merge':
        print(sorting_algos.merge_sort(list))
    elif algo == 'insertion':
        print(sorting_algos.insertion_sort(list))
    elif algo == 'selection':
        print(sorting_algos.selection_sort_in_place(list))

@cli1.command()
@click.option('--algo', help='What type of sorting algorithm would you like to benchmark', required=True)
@click.option('--n', '--num-items', help="Number of items in list you'd like to benchmark", default=100)
def benchmark(algo, n):

    """ Benchmark a certain sorting algorithm"""

    n = int(n)

    if algo  not in sorting_algos.list_of_sorting_algos:
        raise Exception('The algo %s can not be used because it doesn\'t exist. Please enter a valid sorting algo from the following list: %s' % (algo, sorting_algos.list_of_sorting_algos))

    list_of_lengths = [1,5,10,50,100,250,500,750,1000,2050,5000,10000,15000]
    if n not in list_of_lengths:
        raise Exception('The provided n: %s is not in the list of supported lengths. Please pick an n from the following list: %s' % (n, list_of_lengths))

    command = 'pytest test/test_' + algo + '_sort.py::test_list_len_' + str(n)
    os.system(command)

@cli1.command()
@click.option('--algo', help='Which sorting algorithm would you like to find the Big O of?', required=True)
def big_o(algo):

    for len in [1,5,10,50,100,250,500,750,1000]:
        len = str(len)
        command = 'pytest --benchmark-json=test/results/' + algo + '_sort_' + len + '.json test/test_' + algo + '_sort.py::test_list_len_' + len
        os.system(command)


cli = click.CommandCollection(sources=[cli1])

if __name__ == "__main__":
    cli()