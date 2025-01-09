diccionario={
    'Ruben':111111,
     'Alba':22222
}
def listadoTelefonos():
   print('Nombre-Teléfono')
   for nombre,telefono in diccionario.items():
       print(nombre + '-' + str(telefono))

def listadoTelefonosOrdenado():
   print('Nombre-Teléfono')
   nuevoDiccionario=dict(sorted(diccionario.items()))
   for nombre,telefono in nuevoDiccionario.items():
       print(nombre + '-' + str(telefono))
 
    
def añadirContacto():
   nombre=(input('Introduzca el nombre del contacto'))
   telefono=int((input('Introduzca el numero de telefono')))
   for telefonoBuscar in diccionario.values():
       if telefonoBuscar==telefono:
           print('El telefono introducido ya esta en la lista.')
           cambio=input('¿Desea cambiarlo?(si/no):')
           cambioFinal=cambio.lower()
           if cambioFinal=='si':
                telefonoFinal=int(input('Introduzca el nuevo telefono'))
                diccionario[nombre]=telefonoFinal
                print(f'Número actualizado para {nombre}.')
                
           else:
               print('Ha decidido no actualizarlo.Se anula el nuevo contacto')
           return
               
       
   diccionario[nombre]=telefono
   print(f'Contacto {nombre} añadido con el teléfono {telefono}.')

def  modificarContacto():
    nombre = input('Introduzca el nombre del contacto que desea modificar: ')
    
    if nombre in diccionario: 
        telefono = int(input('Introduzca el nuevo número de teléfono: '))
        diccionario[nombre] = telefono
        print(f'Número de teléfono actualizado para {nombre}.')
    else:
        print('No se ha encontrado ese nombre.')
        decision = input('¿Desea añadirlo? (si/no): ').lower()
        if decision == 'si':
            telefono = int(input('Introduzca el número de teléfono: '))
            diccionario[nombre] = telefono
            print(f'Contacto {nombre} añadido con el teléfono {telefono}.')
        else:
            print('No se añadió ni se modificó nada.')

        
    
def  eliminarListin():
     diccionario.clear()
     print(diccionario)
    
def buscarTelefono():
   try:
    telefono = int(input('Introduzca el número de teléfono que desea buscar: '))
   except ValueError:
       print('Tienes que introducir un numero')
       return
   for nombre, telefono_guardado in diccionario.items():
        if telefono_guardado == telefono:
            print(f'Contacto: {nombre} - {telefono_guardado}')
            return  # Salir de la función si encontramos el teléfono
   print('No se ha encontrado ningún contacto con ese teléfono.')

def eliminarContacto():
    nombre_guardado = input('Introduzca el nombre que desea eliminar: ')
    for nombre, telefono in diccionario.items():
        if nombre_guardado == nombre:
            print(f'Contacto: {nombre} - {telefono}')
            del diccionario[nombre]
            print('Se ha eliminado el contacto')
            return  # Salir de la función si encontramos el teléfono
    print('No se ha encontrado ningún contacto con ese teléfono.')
        


def menu():
    salida = False
    while not salida:  # Bucle para el menú
        print("\nMenu:")
        print("a Listar todos los contactos")
        print("b Listado ordenado")
        print("c Añadir un nuevo contacto")
        print("d Modificar el telefono de un contacto")
        print("e Buscar un numero de telefono")
        print("f Eliminar un contacto")
        print("g Borra un listin")
        print("h Salir")

        opcion = input('Elija una opcion: ').lower()  # Convertir la entrada a minúsculas

        # Usamos match-case correctamente para comparar con las opciones del menú
        match opcion:
            case 'a':
                listadoTelefonos()
                input('Pulse una letra para continuar')
            case 'b':
                listadoTelefonosOrdenado()
                input('Pulse una letra para continuar')
            case 'c':
                añadirContacto()
                input('Pulse una letra para continuar')
            case 'd':
                modificarContacto()
                input('Pulse una letra para continuar')
            case 'e':
                buscarTelefono()
                input('Pulse una letra para continuar')
            case 'f':
                eliminarContacto()
                input('Pulse una letra para continuar')
            case 'g':
                eliminarListin()
                input('Pulse una letra para continuar')
            case 'h':
                print('Has salido del programa.')
                salida = True 
            case _:
                print('Letra no disponible. Elija una opción válida.')

            
menu()