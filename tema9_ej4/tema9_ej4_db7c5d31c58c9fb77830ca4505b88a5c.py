import re

class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.clave = ''
        self.clave_secreta = ''

    def cambiar_password(self, password):
        if self.validar_password(password):
            self.clave = password
            return True
        else:
            return False

    def login(self, password):
        return self.clave == password

    def validar_password(self, password):
        # Verificar el mínimo de 8 caracteres y máximo de 16
        if len(password) < 8 or len(password) > 16:
            return False

        # Verificar si contiene letras y números
        if not re.search(r'[a-zA-Z]', password) or not re.search(r'\d', password):
            return False

        # Verificar si contiene al menos una letra mayúscula o un carácter especial
        if not re.search(r'[A-Z]', password) and not re.search(r'[!@#$%^&*()]', password):
            return False

        return True

# Ejemplo de uso
usuario = Usuario("JohnDoe", "johndoe@example.com")
print(usuario.cambiar_password("clavesecreta1_"))
print(usuario.login("clavesecreta1_"))
