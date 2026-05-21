"""Este paquete proporciona una simulacion de una db para un sistema_usuarios, con un modulo de validaciones"""
#Metadatos del paquete usuarios
__version__ = "1.0"
__author__ = "Cristian Giraldo Alvarez"
__email__ = "N/A"
__license__ = "MIT"
__gato__ = "Gato"
#Control de exportaciones
__all__ = [
    'DataBase',
    'validar_datos',
    'ValidacionError'
]
# Constantes públicas
VERSION = __version__

#importacion de modulos
from .gestor import DataBase
#importacion de funciones
from .validaciones import validar_datos, ValidacionError



