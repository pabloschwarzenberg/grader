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

        if not re.search(r'[A-Z]', password) and not re.search(r'[^a-zA-Z0-9]', password):
            return False

        return True
        
        
        
usuario = Usuario("ejemplo", "ejemplo@example.com")

if usuario.cambiar_password("Password123#"):
    print("Contraseña cambiada con éxito")
else:
    print("La contraseña no cumple las reglas")

if usuario.login("Password123#"):
    print("Inicio de sesión exitoso")
else:
    print("Inicio de sesión fallido")
