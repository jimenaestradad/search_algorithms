# Benchmark for binary search
# Scenario: list of 100K elements, target NOT found

from searching import binary_search

LIST_100K = list(range(100_000))   # sorted list [0, 1, 2, ..., 99999]
TARGET = -1                        # not present in the list


def my_benchmark_binary(n):
    binary_search(LIST_100K, TARGET)


def test_binary_search_benchmark(benchmark):
    benchmark.pedantic(
        my_benchmark_binary,
        args=(TARGET,),
        rounds=5,
        iterations=5
    )

# Benchmark for linear search
# Scenario: list of 100K elements, target NOT found

from searching import linear_search

LIST_100K = list(range(100_000))   # sorted list [0, 1, 2, ..., 99999]
TARGET = -1                        # not present in the list


def my_benchmark_linear(n):
    linear_search(LIST_100K, TARGET)


def test_linear_search_benchmark(benchmark):
    benchmark.pedantic(
        my_benchmark_linear,
        args=(TARGET,),
        rounds=5,
        iterations=5
    )