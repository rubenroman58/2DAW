def cuentasVocales(cadena):
    vocales = 'aeiouAEIOU'  # Lista de vocales
    contador = 0
    for i in cadena:
        if i in vocales:  # Compara si el carácter está en la cadena de vocales
            contador += 1
    print('El número de vocales en la cadena es: ' + str(contador))  # Convertir contador a string para concatenar

# Solicitar la entrada al usuario
cadena1 = input('Introduzca una cadena para contar las vocales: ') 
cuentasVocales(cadena1)
