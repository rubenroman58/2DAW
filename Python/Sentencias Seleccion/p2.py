numero=int(input('Introduzca el numero de la semana(1-7)'))
match numero:
     case 1:
          print('Lunes')
     case 2:
        print('Martes')
     case 3:
          print('miercoles')
     case 4:
          print('jueves')
     case 5:
          print('viernes')
     case 6:
          print('sabado')

     case 7:
       print('domingo')
     case _ :
        print('El numero introducido no es correcto')


