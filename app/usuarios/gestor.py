from .validaciones import validar_datos, validar_nombre

##=============Clase usuarios ============
class DataBase:
    def __init__(self):
        self.usuarios= []

    def registrar_usuario(self, usuario, edad):
        validar_datos(usuario, edad)
        self.usuarios.append({'nombre':usuario, 'edad':edad})

    def listar_usuarios(self):
        for usuario in self.usuarios:
            print(f"Nombre: {usuario['nombre']}, Edad: {usuario['edad']}")
            
    def obtener_usuario(self, nombre):
        validar_nombre(nombre)
        for usuario in self.usuarios:
            if usuario['nombre'] == nombre:
                return usuario
        return None