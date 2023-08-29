import re

class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.clave = ""

    def cambiar_password(self, password):
        if not re.match("^(?=.*[a-z])(?=.*[A-Z#])(?=.*\d)[a-zA-Z\d#]{8,16}$", password):
            return False
        self.clave = password
        return True

    def login(self, password):
        return self.clave == password