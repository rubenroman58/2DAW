def contarPalabras(cadena):
    contarPalabras=0
    separacion=',. '
    for i in cadena:
        if i in separacion:
            contarPalabras+=1
    print('El numero de palabras introducidas es : ' ,contarPalabras)
    
cadena=input('Introduzca una cadena')
contarPalabras(cadena)