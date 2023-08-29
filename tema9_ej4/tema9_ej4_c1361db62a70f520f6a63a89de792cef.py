#clase usuario
class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.clave = ""

    def cambiar_password(self, password):
        if len(password) < 8 or len(password) > 16:
            return False
        if not any(c.isalpha() for c in password) or not any(c.isdigit() for c in password):
            return False
        if not any(c.isupper() or not c.isalnum() for c in password):
            return False

        self.clave = password
        return True

    def login(self, password):
        return password == self.clave
           