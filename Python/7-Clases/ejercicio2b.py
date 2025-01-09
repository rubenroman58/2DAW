
class Persona:
    def __init__(self, nombre='', apellidos='', dni='', edad=0):
        self.nombre = nombre
        self.apellidos = apellidos
        self.dni = dni
        self.edad = edad
    
    # Setter y Getter para el nombre
    def set_nombre(self, nombre):
        if nombre.strip() == '':
            raise ValueError("El nombre no puede estar vacío")
        self.nombre = nombre.upper()

    def get_nombre(self):
        return self.nombre

    # Setter y Getter para los apellidos
    def set_apellidos(self, apellidos):
        if apellidos.strip() == '':
            raise ValueError("Los apellidos no pueden estar vacíos")
        self.apellidos = apellidos.upper()

    def get_apellidos(self):
        return self.apellidos

    # Setter y Getter para el DNI
    def set_dni(self, dni):
        if dni.strip() == '':
            raise ValueError("El DNI no puede estar vacío")
        self.dni = dni.upper()

    def get_dni(self):
        return self.dni

    # Setter y Getter para la edad
    def set_edad(self, edad):
        if not isinstance(edad, int) or edad <= 0:
            raise ValueError("La edad debe ser un valor entero positivo")
        self.edad = edad

    def get_edad(self):
        return self.edad

    # Método para mostrar los datos de la persona
    def mostrar(self):
        print(f"Nombre: {self.nombre}, Apellidos: {self.apellidos}, DNI: {self.dni}, Edad: {self.edad}")

    # Método para determinar si la persona es mayor de edad
    def mayorDeEdad(self):
        return self.edad >= 18
class Cuenta:
    def __init__(self, titular, cantidad=0.0):
        self._titular = titular
        self._cantidad = cantidad

    # Getters and Setters

    @property
    def get_titular(self):
        return self._titular

    @property
    def get_cantidad(self):
        return self._cantidad

    def ingresar(self, cantidadIngresar):
        if cantidadIngresar > 0:
            self._cantidad += cantidadIngresar

    def retirar(self, cantidadRetirar):
        if cantidadRetirar > 0:
            self._cantidad -= cantidadRetirar

    def mostrar(self):
        print("Información de la cuenta:")
        print(
            f"Titular: {self.get_titular.get_nombre +"  "+  self.get_titular.get_apellidos}"
        )
        print(f"Cantidad: {self.get_cantidad}")
class CuentaJoven(Cuenta):
    def __init__(self,bonificacion, titular, cantidad=0.0):
        super().__init__(titular, cantidad)
        self.bonificacion=bonificacion
        
    
    def mostrar(self):
        super().mostrar()  # Mostrar la información de la cuenta base
        print(f"La bonificación es: {self.bonificacion}")

        
        
    