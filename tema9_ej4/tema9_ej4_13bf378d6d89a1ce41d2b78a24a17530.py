import re

class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.password = ""

    def cambiar_password(self, password):
        if self.validar_password(password):
            self.password = password
            return True
        else:
            return False

    def login(self, password):
        return self.password == password

    def validar_password(self, password):
        # Verificar la longitud de la contraseña
        if len(password) < 8 or len(password) > 16:
            return False

        # Verificar si la contraseña contiene letras y números
        if not any(char.isalpha() for char in password) or not any(char.isdigit() for char in password):
            return False

        # Verificar si la contraseña contiene al menos una letra mayúscula o un carácter especial
        if not any(char.isupper() for char in password) and not re.search("[^a-zA-Z0-9]", password):
            return False

        return True

if __name__ == "__main__":
    usuario = Usuario("pablo", "phschwarzenberg@uc.cl")
    print(usuario.cambiar_password("clave"))               # False
    print(usuario.cambiar_password("clavesecreta1_"))      # True
    print(usuario.cambiar_password("clavesecreta"))        # False
    print(usuario.cambiar_password("clasesecreta1"))       # False
    print(usuario.cambiar_password("claveSecreta1"))       # True
    print(usuario.login("clavesecreta1_"))                  # True
    print(usuario.login("claveSecreta1"))                   # False
