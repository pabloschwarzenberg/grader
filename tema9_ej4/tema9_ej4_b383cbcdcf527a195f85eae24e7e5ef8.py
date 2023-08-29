import re

class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.password = ""

    def cambiar_password(self, password):
        if len(password) < 8 or len(password) > 16:
            return False

        if not re.search(r"[A-Z!@#$%^&*()_+]", password):
            return False

        if not re.search(r"[0-9]", password):
            return False

        self.password = password
        return True

    def login(self, password):
        return self.password == password


if __name__ == "__main__":
    usuario = Usuario("pablo", "phschwarzenberg@uc.cl")
    print(usuario.cambiar_password("clave"))  # False
    print(usuario.cambiar_password("clavesecreta1_"))  # True
    print(usuario.cambiar_password("clavesecreta"))  # False
    print(usuario.cambiar_password("clasesecreta1"))  # False
    print(usuario.cambiar_password("claveSecreta1"))  # True
    print(usuario.login("clavesecreta1_"))  # True
    print(usuario.login("claveSecreta1"))  # False