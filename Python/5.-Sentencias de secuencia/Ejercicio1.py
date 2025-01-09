
salir=True

lista=[]  
while salir==True:
    numero=int(input('Introduzca un numero: '))  
    if numero==0:
        salir=False
    else:
     
        lista.append(numero)  
        
print('Lista : ',lista)
lista.sort()
print('Lista ordenada: ',lista)
lista.reverse()
print('Lista ordenada: ',lista)
    