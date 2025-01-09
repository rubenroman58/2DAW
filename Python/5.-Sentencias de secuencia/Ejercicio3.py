def polindromo(cadena):
        
    if cadena==cadena[::-1]: 
        print('Si es polindromo')
    else:
        print('No es polindromo')


cadena=str(input('Introduzca una cadena'))
polindromo(cadena)
    