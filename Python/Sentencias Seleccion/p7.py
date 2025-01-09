hora=int(input('Introduzca una hora(0-24)'))
if hora >=0 and hora <=24:
    if hora>=7 and hora<=12:
        print('buenos dias')
    elif hora>=12 and hora<=20:
        print('buenos tardes')
    else: 
        print('buenas noches')
else:
    print('valor incorrecto')