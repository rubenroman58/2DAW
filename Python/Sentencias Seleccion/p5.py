edad=int(input('introduzca su edad'))
if edad<5 and edad>=0:
    print('gratis')
elif edad >=5 and edad <18:
    print('tres euros ')
elif edad >=18 and edad <65:
    print('seis euros ')
elif edad>65:
    print('gratis')
else: 
    print('La edad introducida es incorrecta')
