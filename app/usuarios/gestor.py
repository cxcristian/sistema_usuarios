##=============Clase usuarios ============
class DataBase:
    def __init__(self):
        self.usuarios= []
    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def listar_usuarios(self):
        for usuario in self.usuarios:
            print(usuario)
            
    def obtener_usuario(self, nombre):
        for usuario in self.usuarios:
            if usuario.nombre == nombre:
                return usuario
        return None