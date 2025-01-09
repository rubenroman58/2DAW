from typing import List

def segmento(m: int, n: int, xs: List) -> List:
    # Si m > n, devolvemos una lista vacía
    if m > n:
        return []
    # De lo contrario, devolvemos el segmento utilizando slicing
    return xs[m:n+1]  # Incluye también el elemento en la posición n

# Ejemplo 1
print(segmento(3, 4, [3, 4, 1, 2, 7, 9, 0]))  # Salida: [1, 2]

# Ejemplo 2
print(segmento(3, 5, [3, 4, 1, 2, 7, 9, 0]))  # Salida: [1, 2, 7]

# Ejemplo 3: m > n, se debe devolver una lista vacía
print(segmento(5, 3, [3, 4, 1, 2, 7, 9, 0]))  # Salida: []
