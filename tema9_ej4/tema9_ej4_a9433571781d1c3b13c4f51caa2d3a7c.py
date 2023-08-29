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
        # Regla 1: Mínimo 8 caracteres y máximo 16
        if len(password) < 8 or len(password) > 16:
            return False

        # Regla 2: Contiene letras y números
        if not re.search(r'[a-zA-Z]', password) or not re.search(r'\d', password):
            return False

        # Regla 3: Contiene al menos una letra mayúscula o un carácter especial
        if not re.search(r'[A-Z]', password) and not re.search(r'[^a-zA-Z\d]', password):
            return False

        return True


if __name__ == "__main__":
    usuario = Usuario("pablo", "phschwarzenberg@uc.cl")
    print(usuario.cambiar_password("clave"))  # False
    print(usuario.cambiar_password("clavesecreta1_"))  # True
    print(usuario.cambiar_password("clavesecreta"))  # False
    print(usuario.cambiar_password("clasesecreta1"))  # False
    print(usuario.cambiar_password("claveSecreta1"))  # True
    print(usuario.login("clavesecreta1_"))  # True
    print(usuario.login("claveSecreta1"))  # False