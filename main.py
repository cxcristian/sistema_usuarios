from app.usuarios import DataBase, validar_datos, ValidacionError

opciones = (
    "1. Registrar usuarios",
    "2. Listar usuarios",
    "3. Buscar usuario",
    "4. Salir del sistema",
)


def main():
    db = DataBase()
    while True:
        print("=========Menu========")
        for opcion in opciones:
            print(opcion)
        try:
            opcion = int(input("Seleccione una opcion: "))
        except ValueError:
            print("Ingrese un numero entero")
            continue
        finally:
            print("======================")
        match opcion:
            case 1:
                try:
                    nombre = input("Nombre: ")
                    edad = input("Edad: ")
                    db.registrar_usuario(nombre, edad)
                    print("Usuario registrado")
                except ValidacionError as e:
                    print(f"Error: {e}")
            case 2:
                db.listar_usuarios()
            case 3:
                nombre = input("Nombre a buscar: ")
                usuario = db.obtener_usuario(nombre)
                if usuario:
                    print(f"Nombre: {usuario['nombre']}, Edad: {usuario['edad']}")
                else:
                    print("Usuario no encontrado")
            case 4:
                print("Saliendo del sistema")
                break
            case _:
                print("Opcion no valida")


if __name__ == "__main__":
    main()