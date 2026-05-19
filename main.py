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