class Persona():
    def __init__(self, nombre, direccion,telefono):
     self.nombre =nombre
     self.direccion =direccion
     self.telefono =telefono
    
    def __str__(self):
        return f"Nombre: {self.nombre}, Dirección: {self.direccion}, Teléfono: {self.telefono}"
      # Getter para el nombre
    def get_nombre(self):
        return self.nombre
    
    # Setter para el nombre
    def set_nombre(self, nombre):
        self._nombre = nombre
    
    # Getter para la dirección
    def get_direccion(self):
        return self.direccion
    
    # Setter para la dirección
    def set_direccion(self, direccion):
        self._direccion = direccion
    
    # Getter para el teléfono
    def get_telefono(self):
        return self.telefono
    
    # Setter para el teléfono
    def set_telefono(self, telefono):
        self._telefono = telefono
     
contactos={'RUBEN':Persona('ruben','calle hueva',3456),
           'Alba':Persona('alb','calle hueva',3333)}

def listadoAlfabetico():
    nuevoDiccionario=dict(sorted(contactos.items()))
    for nombre, persona in nuevoDiccionario.items():
        print('Nombre-Persona')
        print(nombre +'--'+str(persona))
    
    
def añadirContactos():
    nombre=input('Introduzca el nombre')  
    direccion=input('Introduzca su direccion')
    try:
        telefono=int(input('Introduzca el telefono'))
    except ValueError:
       print('Tienes que introducir un numero')
       return
     # Verificar si el teléfono ya está en el diccionario
    for persona in contactos.values():
        if persona.get_telefono() == telefono:
            print('El telefono introducido ya esta en la lista.')
            return  # Salir de la función si el teléfono ya existe

    # Si no se encuentra el teléfono, añadir el nuevo contacto
    contactos[nombre] = Persona(nombre, direccion, telefono)
    print(f'El contacto {nombre} ha sido añadido con éxito.')


def modificarContacto():
    nombre = input('Introduzca el nombre: ').upper()  # Convertimos a mayúsculas para la comparación

    if nombre in contactos:  # Verificar si el nombre existe en el diccionario
        # Si el contacto existe, pedimos la nueva dirección y teléfono
        direccion = input('Introduzca la nueva dirección: ')
        try:
            telefono = int(input('Introduzca el nuevo teléfono: '))
        except ValueError:
            print('Tienes que introducir un número válido para el teléfono.')
            return  # Termina la función si hay un error en el teléfono

        # Actualizar el contacto en el diccionario
        contactos[nombre].set_direccion(direccion)
        contactos[nombre].set_telefono(telefono)
        print(f'El contacto {nombre} ha sido modificado con exito.')
    
    else:

        print('No existe ese nombre.')
        decision = input('¿Desea insertarlo? (si/no): ').lower()
        if decision == 'si':
            direccion = input('Introduzca la nueva dirección: ')
            try:
                telefono = int(input('Introduzca el nuevo teléfono: '))
            except ValueError:
                print('Tienes que introducir un número válido para el teléfono.')
                return

            contactos[nombre] = Persona(nombre, direccion, telefono)
            print(f'El contacto {nombre} ha sido añadido con éxito.')
def buscarNumeroTelefono():
        try:
            telefono = int(input('Introduzca el telefono d el apersona que desea buscar: '))
        except ValueError:
            print('Tienes que introducir un número válido para el teléfono.')
            return 
        for datos in contactos.values():
            if  datos.get_telefono()==telefono:
                print('Nombre: '+ str(datos.get_nombre()))
            else:
                print('No se ha encontrado el telefono')
def eliminarContacto():
    nombre = input('Introduzca el nombre del contacto que desea eliminar: ').upper()
    
    if nombre in contactos: 
        del contactos[nombre]  
        print(f'Se ha eliminado el contacto {nombre} del diccionario.')
    else:
        print('No se ha encontrado el contacto.')


def menu():
    salida = False
    while not salida: 
        print("\nMenu:")
        print("a Orden alfabetico")
        print("b Añadir un nuevo contacto")
        print("c Modificar  contacto")
        print("d Buscar un numero de telefono")
        print("e Eliminar un contacto")
        print("f Salir")

        opcion = input('Elija una opcion: ').lower() 

       
        match opcion:
            case 'a':
                listadoAlfabetico()
                input('Pulse una letra para continuar')
            case 'b':
                añadirContactos()
                input('Pulse una letra para continuar')
            case 'c':
                modificarContacto()
                input('Pulse una letra para continuar')
            case 'd':
                buscarNumeroTelefono()
                input('Pulse una letra para continuar')
            case 'e':
                eliminarContacto()
                input('Pulse una letra para continuar')
            case 'f':
               print('Has salido del programa.')
               salida = True  
            case _:
                print('Letra no disponible. Elija una opción válida.')

            
menu()