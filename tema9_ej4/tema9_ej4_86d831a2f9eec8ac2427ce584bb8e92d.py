import re

class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.clave = ''

    def cambiar_password(self, password):
        if len(password) < 8 or len(password) > 16:
            return False

        if not re.search("[a-z]", password) or not re.search("[0-9]", password) or (not re.search("[A-Z]", password) and not re.search("[_!@#$%^&*?]", password)):
            return False

        self.clave = password
        return True

    def login(self, password):
        return self.clave == password

usuario = Usuario("ejemplo", "ejemplo@ejemplo.com")
if usuario.cambiar_password("clavesecreta1_"):
    print(usuario.login("clavesecreta1_")) # True
else:
    print("La contraseña no cumple con los requisitos")
