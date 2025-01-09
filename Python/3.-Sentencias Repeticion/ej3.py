x = int(input('Introduzca un numero: '))
numeroMinimo = x
numeroMaximo = x
numerosIntroducidos = 0
sumaNumeros = 0
while x != 0:
    numerosIntroducidos += 1
    sumaNumeros += x
    if numeroMaximo < x:
        numeroMaximo = x
    if numeroMinimo > x:
        numeroMinimo = x
    media = sumaNumeros/numerosIntroducidos
    print('El total de numeros introducidos es: ' + str(numerosIntroducidos))
    print('El valor minimo es: ', numeroMinimo)
    print('El valor maximo es: ', numeroMaximo)
    print('La  suma de todos los numeros  es: ', sumaNumeros)
    print('La media es: ', round(media, 2))
    x = int(input('Introduzca otro numero (0 para terminar): '))

else:
    print('El programa ha acabado')
