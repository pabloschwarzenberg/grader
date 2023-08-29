class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.clave = ""

    def cambiar_password(self, password):
        if len(password) < 8 or len(password) > 16:
            return False

        if not any(char.isalpha() for char in password) or not any(char.isdigit() for char in password):
            return False

        if not any(char.isupper() for char in password) and not any(char in "#$%&@!" for char in password):
            return False

        self.clave = password
        return True

    def login(self, password):
        return self.clave == password
