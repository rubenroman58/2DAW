from typing import List

def extremos(n: int, xs: List) -> List:
    # Obtener los n primeros elementos y los n últimos elementos
    return xs[:n] + xs[-n:]

# Ejemplo
print(extremos(3, [2, 6, 7, 1, 2, 4, 5, 8, 9, 2, 3]))  # Salida: [2, 6, 7, 9, 2, 3]
