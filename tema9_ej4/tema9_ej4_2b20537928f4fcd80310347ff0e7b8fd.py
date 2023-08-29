class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.clave = ""

    def cambiar_password(self, password):
        if 8 <= len(password) <= 16 and any(char.isalpha() for char in password) and any(char.isdigit() for char in password) and (any(char.isupper() for char in password) or any(not char.isalnum() for char in password)):
            self.clave = password
            return True
        else:
            return False

    def login(self, password):
        return password == self.clave
