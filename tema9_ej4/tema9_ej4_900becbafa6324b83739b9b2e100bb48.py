import re

class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.clave = ""

    def cambiar_password(self, password):
        if self.validar_password(password):
            self.clave = password
            return True
        else:
            return False

    def login(self, password):
        return password == self.clave

    def validar_password(self, password):
        # Verificar longitud mínima y máxima
        if len(password) < 8 or len(password) > 16:
            return False

        # Verificar letras y números
        if not re.search(r'[a-zA-Z]', password) or not re.search(r'\d', password):
            return False

        # Verificar al menos una letra mayúscula o carácter especial
        if not re.search(r'[A-Z!@#$%^&*()\-_=+{};:,<.>]', password):
            return False

        return True