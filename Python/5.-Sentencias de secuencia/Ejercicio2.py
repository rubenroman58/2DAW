
salir=True

lista=[]  
while salir==True:
    cadena=str(input('Introduzca un cadena(vacia para salir): '))  
    if cadena==" ":
        salir=False
    else:
     
        lista.append(cadena)  
        
print('Lista : ',lista)
lista.sort()
print('Lista ordenada: ',lista)
lista.reverse()
print('Lista ordenada: ',lista)
    
