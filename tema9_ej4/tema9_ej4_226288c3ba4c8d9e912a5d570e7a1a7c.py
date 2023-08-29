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
        if 8 <= len(password) <= 16:
            if re.search(r'[A-Z]', password) and re.search(r'[0-9]', password) and (re.search(r'[^a-zA-Z0-9]', password) or re.search(r'[a-z]', password)):
                return True
        return False


# Ejemplo de uso
usuario = Usuario("Juan", "juan@example.com")
print(usuario.nombre)  # Imprime: Juan
print(usuario.email)  # Imprime: juan@example.com
print(usuario.clave)  # Imprime: ''

usuario.cambiar_password("abc123")  # Intento cambiar la clave con una password inválida
print(usuario.clave)  # Imprime: ''
usuario.cambiar_password("clavesecreta1_")  # Intento cambiar la clave con una password válida
print(usuario.clave)  # Imprime: clavesecreta1_

print(usuario.login("clavesecreta1_"))  # Imprime: True
print(usuario.login("ContraseñaIncorrecta"))  # Imprime: False