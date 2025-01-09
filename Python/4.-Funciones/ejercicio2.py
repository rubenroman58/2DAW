def mostrarMenu():
    opcion = True
    while opcion:
        print('1) Mostrar un rombo')
        print('2) Adivinar un número')
        print('3) Resolver una ecuación de segundo grado')
        print('4) Tabla de números')
        print('5) Cálculo del número factorial de un número')
        print('6) Cálculo de un número de la sucesión de Fibonacci')
        print('7) Tabla de multiplicar')
        print('8) Salir')

        try:
            intro = int(input('Introduzca el número de la opción: '))
        except ValueError:
            print("Por favor, introduzca un número válido.")
            continue

        match intro:
            case 1:
                mostrarRombo()
            case 2:
                adivinarNumero()
            case 3:
                ecuacionSegundoGrado()
            case 4:
                tablaNumeros()
            case 5:
                factorialNumero()
            case 6:
                fibonacci()
            case 7:
                tablamultiplicar()
            case 8:
                print('Has salido del programa')
                opcion = False
            case _:
                print("Opción no válida, por favor seleccione un número entre 1 y 8.")
