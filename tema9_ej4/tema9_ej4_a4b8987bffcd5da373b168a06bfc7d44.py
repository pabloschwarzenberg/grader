import string

class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.clave = ""

    def cambiar_password(self, password):
        if not (8 <= len(password) <= 16):
            return False
        if not any(c.isalpha() for c in password):
            return False
        if not any(c.isdigit() for c in password):
            return False
        if not any(c.isupper() for c in password) and not any(c in string.punctuation for c in password):
            return False
        self.clave = password
        return True

    def login(self, password):
        return password == self.clave
