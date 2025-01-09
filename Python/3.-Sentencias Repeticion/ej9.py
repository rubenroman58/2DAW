x = int(input('Introduzca un numero impar'))

if (x % 2 != 0):
    for i in range(1, x+1, 2):

        espacios = (x - i) // 2

        print(' ' * espacios + '*' * i)

else:
    print('El numero introducido es par')
