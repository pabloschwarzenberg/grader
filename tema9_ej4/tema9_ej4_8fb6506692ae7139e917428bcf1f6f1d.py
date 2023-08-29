class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.clave = ""

    def cambiar_password(self, password):
        # Verificar longitud de la password
        if len(password) < 8 or len(password) > 16:
            return False

        # Verificar si contiene letras y números
        if not any(c.isalpha() for c in password) or not any(c.isdigit() for c in password):
            return False

        # Verificar si contiene al menos una letra mayúscula o un carácter especial
        if not any(c.isupper() for c in password) and not any(not c.isalnum() for c in password):
            return False

        self.clave = password
        return True

    def login(self, password):
        return self.clave == password
           