import re

class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.clave = ''

    def cambiar_password(self, password):
        if len(password) < 8 or len(password) > 16:
            return False

        if not re.search('[a-zA-Z0-9]', password):
            return False

        if not re.search('[A-Z!@#$%^&*()_]', password):
            return False

        self.clave = password
        return True

    def login(self, password):
        return self.clave == password

usuario = Usuario("John Doe", "john@example.com")

if usuario.cambiar_password("Abcdef123!"):
    print("Password cambiada exitosamente")
else:
    print("La password no cumple las reglas")

if usuario.login("Abcdef123!"):
    print("Login exitoso")
else:
    print("Login fallido")

           