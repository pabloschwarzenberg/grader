class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        pass

    def login(self,password):
        pass

if __name__ == "__main__":
    usuario=Usuario("pablo","phschwarzenberg@uc.cl")
    print(usuario.cambiar_password("clave"))
    print(usuario.cambiar_password("clavesecreta1_"))
    print(usuario.cambiar_password("clavesecreta"))
    print(usuario.cambiar_password("clasesecreta1"))
    print(usuario.cambiar_password("claveSecreta1"))
    print(usuario.login("clavesecreta1_"))
    print(usuario.login("claveSecreta1"))

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
        if len(password) < 8 or len(password) > 16:
            return False

        if not re.search(r"\d", password):
            return False

        if not re.search(r"[A-Z!@#$%^&*()_+]", password):
            return False

        return True

if __name__ == "__main__":
    usuario = Usuario("pablo", "phschwarzenberg@uc.cl")
    print(usuario.cambiar_password("clave"))  # Output: False
    print(usuario.cambiar_password("clavesecreta1_"))  # Output: True
    print(usuario.cambiar_password("clavesecreta"))  # Output: False
    print(usuario.cambiar_password("clasesecreta1"))  # Output: False
    print(usuario.cambiar_password("claveSecreta1"))  # Output: True
    print(usuario.login("clavesecreta1_"))  # Output: True
    print(usuario.login("claveSecreta1"))  # Output: False