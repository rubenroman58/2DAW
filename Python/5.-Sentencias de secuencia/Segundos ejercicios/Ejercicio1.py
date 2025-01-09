def contarVocales(cadena):
    contarVocales=0
    vocales='aeiouAEIOU'
    for i in cadena:
        if i in vocales:
            contarVocales+=1
    print('El numero de vocales es : ' ,contarVocales)
    
cadena=input('Introduzca una cadena')
contarVocales(cadena)
        