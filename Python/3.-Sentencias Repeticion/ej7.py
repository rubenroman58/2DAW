cadena = str(input('Introduzca una cadena de rexto: '))
letra = str(input('Introduzca la letra que desea buscar: '))
contador = 0
for i in cadena:
        if (i == letra):
            contador += 1
print('La letra ha aparecido un total de: ',contador)
