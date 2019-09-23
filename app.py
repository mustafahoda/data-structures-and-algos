import click
from src.SortingAlgorithms import sorting_algos

import ast

@click.command()
@click.option('--algo', default='quick', help='What type of algorithm would you like to use to sort this list?')
@click.argument('list')
def sort_list(algo, list):
    """A program that allows you to do common sorting algorithms for lists"""

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

# @click.command()
# def benchmark():
#     click.echo("We're gonna benchmark")

if __name__ == "__main__":
    sort_list()
    # benchmark()