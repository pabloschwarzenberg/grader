class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.clave = ""

    def cambiar_password(self, password):
        if len(password) < 8 or len(password) > 16:
            return False
        if not any(char.isupper() or not char.isalnum() for char in password):
            return False

        self.clave = password
        return True

    def login(self, password):
        return self.clave == password
