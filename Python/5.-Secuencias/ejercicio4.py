from typing import List

def rota(n: int, xs: List) -> List:
    n = n % len(xs)
    return xs[n:] + xs[:n]
print(rota(1, [3, 2, 5, 7]))  # [2, 5, 7, 3]
print(rota(2, [3, 2, 5, 7]))  # [5, 7, 3, 2]
print(rota(3, [3, 2, 5, 7]))  # [7, 3, 2, 5]