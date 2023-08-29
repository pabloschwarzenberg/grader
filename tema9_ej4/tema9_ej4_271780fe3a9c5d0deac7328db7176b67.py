class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.clave = ""

    def cambiar_password(self, password):
        if len(password) < 8 or len(password) > 16:
            return False
        if not any(n.isalpha() for n in password) or not any(n.isdigit() for n in password):
            return False
        if not any(n.isupper() or not n.isalnum() for n in password):
            return False

        self.clave = password
        return True

    def login(self, password):
        return password == self.clave
