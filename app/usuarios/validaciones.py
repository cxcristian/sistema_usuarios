class ValidacionError(Exception):
    pass


class DataValidationError(ValidacionError):
    pass


class AgeValidationError(ValidacionError):
    pass


class EmptyNameError(ValidacionError):
    pass


def validar_nombre(nombre):
    try:
        if nombre is None:
            raise EmptyNameError("El nombre no puede ser None.")
        nombre.strip()
    except AttributeError:
        raise DataValidationError("El nombre debe ser una cadena de texto.")
    else:
        if nombre.strip() == "":
            raise EmptyNameError("El nombre no puede estar vacío.")
        return True


def validar_edad(edad):
    try:
        if isinstance(edad, str):
            if edad.strip().lower() in ("null", "none", ""):
                raise AgeValidationError("La edad no puede ser nula o vacía.")
            edad = int(edad)
        if edad is None:
            raise AgeValidationError("La edad no puede ser None.")
        if edad < 0 or edad > 120:
            raise AgeValidationError("La edad debe estar entre 0 y 120 años.")
    except (TypeError, ValueError):
        raise AgeValidationError("La edad debe ser un número entero.")
    else:
        return True

def validar_datos(nombre, edad):
    validar_nombre(nombre)
    validar_edad(edad)
    return True
    