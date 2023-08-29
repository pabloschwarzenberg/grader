import re

class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.clave = ''

    def cambiar_password(self, password):
        if len(password) < 8 or len(password) > 16:
            return False

        if not re.search(r'[A-Z!@#$%^&*()?/|}{~:><=_+]', password):
            return False

        if not re.search(r'[a-zA-Z]', password) or not re.search(r'\d', password):
            return False

        self.clave = password
        return True

    def login(self, password):
        return self.clave == password

# Ejemplo de uso
usuario = Usuario("Juan", "juan@example.com")
print(usuario.cambiar_password("password"))  # Output: False
print(usuario.login("password"))  # Output: False

print(usuario.cambiar_password("StrongPassword1"))  # Output: True
print(usuario.login("StrongPassword1"))  # Output: True
           