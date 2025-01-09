# Recoger el número ingresado por el usuario
n = int(input("Introduce un número: "))

# Generar el triángulo de secuencias decrecientes de números impares
for i in range(1, n + 1):
    num = 2 * i - 1  # Primer número impar de la fila
    for j in range(i):  # Imprimir los números impares en orden decreciente
        print(num, end=" ")
        num -= 2  # Disminuir en 2 para obtener el siguiente número impar
    print() 