filas = int(input('Introduzca el numero de filas: '))
columnas = int(input('Introduzca el numero de columnas: '))
celdas = 1
for i in range(1, filas+1):
    for j in range(1, columnas+1):
      print(celdas, end="\t")
      celdas+=1
    print()

