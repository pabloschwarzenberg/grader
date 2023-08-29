
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

    def login(self, password):
        return self.clave == password

    def validar_password(self, password):
        if len(password) < 8 or len(password) > 16:
            return False

        if not any(char.isdigit() for char in password):
            return False

        if not any(char.isalpha() for char in password):
            return False

        if not re.search(r"[A-Z]|[^a-zA-Z0-9]", password):
            return False

        return True


# Ejemplo de uso
usuario = Usuario("Juan", "juan@example.com")
print(usuario.nombre)  # Imprime: Juan
print(usuario.email)  # Imprime: juan@example.com
print(usuario.clave)  # Imprime: ''

usuario.cambiar_password("abc123")  # Intentamos cambiar la password con una que no cumple las reglas
print(usuario.clave)  # Imprime: ''
print(usuario.login("abc123"))  # Imprime: False (no coincide con la clave actual)

usuario.cambiar_password("Password#123")  # Cambiamos la password con una que cumple las reglas
print(usuario.clave)  # Imprime: Password#123
print(usuario.login("Password#123"))  # Imprime: True (coincide con la clave actual)
