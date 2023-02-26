from functools import lru_cache
import pytest

@lru_cache(maxsize=10000)
def fibonacci(n: int):
    if not isinstance(n, int) or n < 1:
        raise ValueError("Input must be a positive integer.")
    return 1 if (n == 1 or n == 2) else fibonacci(n - 1) + fibonacci(n - 2)

#Définir les tests unitaires avec pytest
def test_fibonacci():

    assert fibonacci(1) == 1

    assert fibonacci(2) == 1

    assert fibonacci(3) == 2

    assert fibonacci(4) == 3

    assert fibonacci(5) == 5

    assert fibonacci(6) == 8
    
    assert fibonacci(7) == 13
    
    assert fibonacci(8) == 21