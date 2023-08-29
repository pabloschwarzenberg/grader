class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.clave = ""

    def cambiar_password(self, password):
        if len(password) < 8 or len(password) > 16:
            return False

        has_uppercase = any(char.isupper() for char in password)
        has_special_char = any(not char.isalnum() for char in password)

        if not (has_uppercase or has_special_char):
            return False

        self.clave = password
        return True

    def login(self, password):
        return self.clave == password
