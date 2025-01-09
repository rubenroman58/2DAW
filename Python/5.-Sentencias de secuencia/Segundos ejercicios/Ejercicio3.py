def sumaNumeros(a, b):
    suma = a+b
    return suma


numero1 = int(input('Introduzca el primer numero que desea sumar'))
numero2 = int(input('Introduzca el segundo numero que desea sumar'))

suma12 = sumaNumeros(numero1, numero2)
numero3 = int(input('Introduzca el tercer numero que desea sumar'))
numeroFinal = sumaNumeros(suma12, numero3)
print('La suma de los tres numeros es: ', numeroFinal)
