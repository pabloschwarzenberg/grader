import re

class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.password = ''
        self.email = email

    def cambiar_password(self, password):
        # Revisa si la longitud de la password es adecuada
        if not 8 <= len(password) <= 16:
            return False
        # Revisa si la password contiene letras y números
        if not re.search(r'\d', password) or not re.search(r'[a-zA-Z]', password):
            return False
        # Revisa si la password contiene una letra mayúscula o un carácter especial
        if not re.search(r'[A-Z_!@#$%^&*(),.?":{}|<>]', password):
            return False
        # Si todas las verificaciones son correctas, cambia la password
        self.password = password
        return True

    def login(self, password):
        return self.password == password
