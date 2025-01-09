def mayorRectangulo(r1: tuple[float, float], r2: tuple[float, float]) -> tuple[float, float]:
    # Calculamos el área de ambos rectángulos
    area_r1 = r1[0] * r1[1]
    area_r2 = r2[0] * r2[1]
    
    # Comparamos las áreas y devolvemos el rectángulo con la mayor área
    if area_r1 > area_r2:
        return r1
    else:
        return r2

# Ejemplos de uso
print(mayorRectangulo((4, 6), (3, 7)))  # Salida: (4, 6)
print(mayorRectangulo((4, 6), (3, 8)))  # Salida: (4, 6)
print(mayorRectangulo((4, 6), (3, 9)))  # Salida: (3, 9)
