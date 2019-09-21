import pytest
from SortingAlgorithms import bubble_sort

def test_run_1(benchmark):
    # result = bubble_sort.bubble_sort([5,2,3,1,6,10,7,8])
    # assert "LOL" == result

    benchmark(bubble_sort.bubble_sort, [5,2,3,1,6,10,7,8])