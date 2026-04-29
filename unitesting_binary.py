'''
Unit testing - Binary Search
'''

import pytest
from searching import binary_search


BINARY_SEARCH_TEST_CASES = [
    # (arr, target, expected_index)
    ([10, 20, 30, 40, 50], 10, 0),   # Encontrado al inicio
    ([10, 20, 30, 40, 50], 30, 2),   # Encontrado en el medio
    ([10, 20, 30, 40, 50], 50, 4),   # Encontrado al final
    ([10, 20, 30, 40, 50], 99, -1),  # No encontrado
    ([], 5, -1),                     # Lista vacía (caso límite)
    ([7], 7, 0),                     # Un solo elemento, encontrado
    ([7], 3, -1),                    # Un solo elemento, no encontrado
]


@pytest.mark.parametrize("arr, target, expected", BINARY_SEARCH_TEST_CASES)
def test_binary_search(arr, target, expected):
    assert binary_search(arr, target) == expected