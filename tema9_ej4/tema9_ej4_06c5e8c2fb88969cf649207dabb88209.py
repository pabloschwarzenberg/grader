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
        return self.clave == password

    def validar_password(self, password):
        if len(password) < 8 or len(password) > 16:
            return False

        if not re.search("[a-zA-Z0-9]", password):
            return False

        if not re.search("[A-Z]", password) and not re.search("[!@#$%^&*()_+=\-{}\[\]|\\:;\"'<>,.?/]", password):
            return False

        return True
