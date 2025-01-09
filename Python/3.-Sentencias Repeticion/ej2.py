numero = int(input('Introduzca un número para calcular su factorial: '))

resultado = 1  
for numero1 in range(1, numero + 1):
    resultado *= numero1 

print(f'El factorial de {numero} es: {resultado}')