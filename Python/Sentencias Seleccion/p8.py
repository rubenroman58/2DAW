mes=int(input('introduzca el mes del año'))
match mes:
     case 1:
          print('31')
     case 2:
        print('28')
     case 3:
          print('31')
     case 4:
          print('30')
     case 5:
          print('31')
     case 6:
          print('30')

     case 7:
       print('31')
     case 8:
       print('31')
     case 9:
       print('30')
     case 10:
       print('31')
     case 11:
       print('30')
     case 12:
       print('31')
     case _ :
        print('El mes introducido no es correcto')