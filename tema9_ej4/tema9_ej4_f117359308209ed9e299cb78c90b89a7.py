import re

class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.clave = ''

    def cambiar_password(self, password):
        if self.validar_password(password):
            self.clave = password
            return True
        else:
            return False

    def validar_password(self, password):
        if 8 <= len(password) <= 16 and re.search(r'[a-zA-Z0-9]', password) and (re.search(r'[A-Z]', password) or re.search(r'[^a-zA-Z0-9]', password)):
            return True
        else:
            return False

    def login(self, password):
        return self.clave == password


# Ejemplo de uso
usuario1 = Usuario("Juan123", "juan@example.com")
print(usuario1.cambiar_password("abc123XYZ"))  # True
print(usuario1.clave)  # "abc123XYZ"
print(usuario1.login("abc123XYZ"))  # True
print(usuario1.login("abc123xyz"))  # False (mayúscula requerida)
print(usuario1.login("abc12XYZ"))  # False (mínimo de 8 caracteres)
