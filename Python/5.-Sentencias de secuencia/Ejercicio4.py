cadena1 = str(input('Introduzca la primera cadena'))
cadena2 = str(input('Introduzca la segunda cadena'))
cadena3 = str(input('Quieres tener en cuenta las mayusculas y minusculas'))
cadena3Nueva = cadena3.lower()
match cadena3Nueva:
    case "si":
             if cadena1 == cadena2[::-1]:
                print('Si es polindromo')
             else:
                print('No es polindromo')
    case "no":
              nuevaCadena1 = cadena1.lower()
              nuevaCadena2 = cadena2.lower()
              if nuevaCadena1 == nuevaCadena2[::-1]:
                print('Si es polindromo')
              else:
                print('No es polindromo')     
    case _:
              print('Valor incorrecto(debe introducir(si,no))')  
