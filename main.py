#Leer las variables de entorno
from dotenv import load_dotenv as ld
import os
ld()
APP_NAME= os.getenv("APP_NAME")
APP_VERSION= os.getenv("APP_VERSION")
ADMIN_USER= os.getenv("ADMIN_USER")
ADMIN_PASSWORD= os.getenv("ADMIN_PASSWORD")

print(f"Nombre: {APP_NAME}")
print(f"Versión: {APP_VERSION}")
print(f"Usuario admin: {ADMIN_USER}")

opciones = (("1. Registrar usuarios"), ("2. Listar usuarios"), ("3. Buscar usuario"))
#=========================Menu===========================
def main():
    while True:
        print("=========Menu========")
        for opcion in opciones:
            print(opcion)
        try:
            opcion = int(input("Seleccione una opcion:"))
        except ValueError:
            print("Ingrese un numero entero")
            continue
        finally:
            print("======================")
        match opcion:
            case 1:
                print("1.Registrar usuarios")
            case 2:
                print("2.Listar usuarios")
            case 3:
                print("3.Buscar usuario")
            case _:
                print("Opcion no valida")

if __name__ == "__main__":
    main()