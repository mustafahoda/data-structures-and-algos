from src.SortingAlgorithms import sorting_algos

def test_list_len_1(benchmark, list_len_1, ):
    results = benchmark.pedantic(sorting_algos.quick_sort, args=(list_len_1,), iterations = 2, rounds = 5)
    sorted(list_len_1) == results

def test_list_len_5(benchmark, list_len_5, ):
    results = benchmark.pedantic(sorting_algos.quick_sort, args=(list_len_5,), iterations = 2, rounds = 5)
    sorted(list_len_5) == results

def test_list_len_10(benchmark, list_len_10, ):
    results = benchmark.pedantic(sorting_algos.quick_sort, args=(list_len_10,), iterations=2, rounds=5)
    sorted(list_len_10) == results


def test_list_len_100(benchmark, list_len_100, ):
    results = benchmark.pedantic(sorting_algos.quick_sort, args=(list_len_100,), iterations=2, rounds=5)
    sorted(list_len_100) == results


def test_list_len_500(benchmark, list_len_500, ):
    results = benchmark.pedantic(sorting_algos.quick_sort, args=(list_len_500,), iterations=2, rounds=5)
    sorted(list_len_500) == results


def test_list_len_1000(benchmark, list_len_1000, ):
    results = benchmark.pedantic(sorting_algos.quick_sort, args=(list_len_1000,), iterations=2, rounds=5)
    sorted(list_len_1000) == results


def test_list_len_10000(benchmark, list_len_10000, ):
    results = benchmark.pedantic(sorting_algos.selection_sort, args=(list_len_10000,), iterations=2, rounds=5)
    sorted(list_len_10000) == results


def test_list_len_15000(benchmark, list_len_15000, ):
    results = benchmark.pedantic(sorting_algos.selection_sort, args=(list_len_15000,), iterations=2, rounds=1)
    sorted(list_len_15000) == results
