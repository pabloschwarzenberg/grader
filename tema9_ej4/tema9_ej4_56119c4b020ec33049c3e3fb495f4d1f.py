import re

class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.password = ""

    def cambiar_password(self, password):
        if self.validar_password(password):
            self.password = password
            return True
        else:
            return False

    def login(self, password):
        return self.password == password

    def validar_password(self, password):
        if len(password) < 8 or len(password) > 16:
            return False

        if not any(char.isupper() or not char.isalnum() for char in password):
            return False

        return True
           