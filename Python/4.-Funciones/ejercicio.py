def tablamultiplicar():
    numero = int(input('Introduzca el numero de la tabla'))
    for i in range(0, 11, 1):
        print(numero, ' * ', i, '= ', numero*i)
    input('Toque una tecla para continuar')


def ecuacionSegundoGrado():
    import math
    print("Resolver la ecuación de segundo grado: ax^2 + bx + c = 0")

    # Leer coeficientes
    a = float(input("Introduzca el coeficiente a: "))
    b = float(input("Introduzca el coeficiente b: "))
    c = float(input("Introduzca el coeficiente c: "))

    # Calcular el discriminante
    D = b**2 - 4*a*c

    # Evaluar las soluciones
    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        print(f"Las soluciones son: x1 = {x1} y x2 = {x2}")
    elif D == 0:
        x = -b / (2 * a)
        print(f"La solución doble es: x = {x}")
    else:
        print("No hay soluciones reales.")


def tablaNumeros():
    import random

    filas = int(input('Introduce un numero de filas'))
    columnas = int(input('Introduce un numero de columnas'))
    for i in range(filas):
        for j in range(columnas):
            numero = random.randint(0, 100)
            print(numero, end='\t')
        print()
    input('Toque una tecla para continuar')


def factorialNumero():
    numero = int(input('Introduzca el numero para calcular el factorial'))
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    print(resultado)
    input('Toque una tecla para continuar')


def adivinarNumero():
    import random
    numeroAleatorio = random.randint(1, 100)
    numero = None
    while numeroAleatorio != numero:
        numero = int(input('Introduzca el numero para adivinar'))
        if numero > numeroAleatorio:
            print('El número es MANOR')
        elif numero < numeroAleatorio:
            print('El número es MEYOR')
        else:
            print('¡Has adivinado el número!')
    print('El número era:', numeroAleatorio)
    input('Toque una tecla para continuar')


def mostrarRombo():
    esCorrecto = False
    while esCorrecto == False:  # Cambiamos a while not esCorrecto
        numero = int(input('Introduzca un número impar: '))
        if numero % 2 == 0:  # Comprobamos si es par
            print('Número par. Vuelva a introducir un número.')
        else:
            for i in range(1, numero+1, 2):
                espacios = (numero-i)//2
                print(' '*espacios+'*'*i)
            for i in range(numero-2, 0, -2):
                espacios2 = (numero-i)//2
                print(' '*espacios2+'*'*i)
            esCorrecto = True  # Si es impar, salimos del bucle

def fibonacci():
    n = int(input("Introduce la posición del número de Fibonacci que deseas calcular: "))
    if n <= 0:
        print("El número debe ser mayor a 0.")
    elif n == 1:
        print(f"El número de Fibonacci en la posición {n} es 0")
    elif n == 2:
        print(f"El número de Fibonacci en la posición {n} es 1")
    else:
        a, b = 0, 1
        for _ in range(n - 2):
            a, b = b, a + b
        print(f"El número de Fibonacci en la posición {n} es {b}")
    input('Toque una tecla para continuar')



def mostrarMenu():
    letra = True
    while letra:
        print('a) Mostrar un rombo')
        print('b) Adivinar un número.')
        print('c) Resolver una ecuación de segundo grado.')
        print('d) Tabla de números.')
        print('e) Cálculo del número factorial de un número.')
        print('f) Cálculo de un número de la sucesión de Fibonacci.')
        print('g) Tabla de multiplicar.')
        print('h) Salir.')

        intro = input('Introduzca la letra: ')
        letra = intro.lower()

        match letra:
            case 'a':
                mostrarRombo()
            case 'b':
                adivinarNumero()
            case 'c':
                ecuacionSegundoGrado()
            case 'd':
                tablaNumeros()
            case 'f':
                fibonacci()
            case 'e':
                factorialNumero()
            case 'g':
                tablamultiplicar()
            case 'h':
                print('Has salido del programa')
                letra = False


mostrarMenu()
