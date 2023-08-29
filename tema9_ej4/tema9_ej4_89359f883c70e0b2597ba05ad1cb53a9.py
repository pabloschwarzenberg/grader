class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.clave = ""

    def cambiar_password(self, password):
        if len(password) >= 8 and len(password) <= 16:
            if any(c.isupper() or not c.isalnum() for c in password):
                self.clave = password
                return True
        return False

    def login(self, password):
        return password == self.clave
