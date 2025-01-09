numero1=int(input('Introduzca el primer numero: '))
numero2=int(input('Introduzca el segundo numero: '))
numero3=int(input('Introduzca el tercer numero: '))

if numero1 > numero2 and numero1 > numero3:
    print(numero1 , 'es el mayor numero')
elif numero2>numero3 and numero2>numero1:
      print(numero2 , 'es el mayor numero')
     
else:
     print(numero3 ,'es el mayor numero')

if numero1 < numero2 and numero1 < numero3:
    print(numero1 , 'es el menor numero')
elif numero2<numero3 and numero2<numero1:
      print(numero2 , 'es el menor numero')
     
else:
     print(numero3 ,'es el mmenor numero')