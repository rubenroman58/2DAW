cadena='hola ruben'
print(cadena[1:8])
print(cadena[1:8])
print(cadena[1:8])
print(cadena[::-1])
print(cadena.title())
cadena2='HOLA CARACOLA'
print(cadena2.lower())
print(cadena.upper())
cadena3='que pasa'
print(cadena3.title())
print(cadena3.capitalize())
cadena4='dime algo interesante'
print(cadena4.strip())
print(cadena4.startswith('e'))
print(cadena4.endswith('e'))
print(cadena4.replace('dime','interesante'))

cadena5=input('Introduzca una cadena')
vocales='aeiouAEIOU'
for i in vocales:
    cadena5=cadena5.replace(i,'*')
print(cadena5)

lista=[1,2,3,4,4,4,4]

print(lista.index(5))