def cuentasVocales(cadena):
    palabra = ',. '  # Lista de vocales
    contador = 1
    for i in cadena:
        if i in palabra:  # Compara si el carácter está en la cadena de vocales
            contador += 1
    print('El numero de palabras es: ' + str(contador))  # Convertir contador a string para concatenar

# Solicitar la entrada al usuario
cadena1 = input('Introduzca una cadena para contar las palabras: ') 
cuentasVocales(cadena1)
