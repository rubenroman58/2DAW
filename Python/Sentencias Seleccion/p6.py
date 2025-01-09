nota=float(input('introduzca la nota(decimal)'))
if nota<5 and nota >=0:
    print('suspenso')
elif nota >=5 and nota< 6:
    print('suficiente ')
elif nota >=6 and nota< 7:
    print('bien ')
elif nota >=7 and nota< 9:
    print('notable ')
elif nota >=9 and nota< 10:
    print('sobresaliente ')
elif nota==10:
    print('honor')
else:
    print('El numero introducido no es correcto')
