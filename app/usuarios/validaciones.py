class ValidacionError(Exception):
    pass


class DataValidationError(ValidacionError):
    pass


class AgeValidationError(ValidacionError):
    pass


class EmptyNameError(ValidacionError):
    pass


def validar_nombre(nombre):
    if nombre is None:
        raise EmptyNameError("El nombre no puede ser None.")
    if not isinstance(nombre, str):
        raise DataValidationError("El nombre debe ser una cadena de texto.")
    if nombre.strip() == "":
        raise EmptyNameError("El nombre no puede estar vacío.")
    return True


def validar_edad(edad):
    if edad is None:
        raise AgeValidationError("La edad no puede ser None.")
    if not isinstance(edad, int):
        raise AgeValidationError("La edad debe ser un número entero.")
    if edad < 0 or edad > 120:
        raise AgeValidationError("La edad debe estar entre 0 y 120 años.")
    return True


def validar_datos(nombre, edad):
    validar_nombre(nombre)
    validar_edad(edad)
    return True
    