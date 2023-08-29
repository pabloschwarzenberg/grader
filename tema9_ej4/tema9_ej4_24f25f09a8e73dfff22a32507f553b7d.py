import re

class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.password = ""

    def cambiar_password(self, password):
        if not 8 <= len(password) <= 16:
            return False
        if not re.search(r"[A-Za-z0-9]", password):
            return False
        if not (re.search(r"[A-Z]", password) or re.search(r"[^A-Za-z0-9]", password)):
            return False
        self.password = password
        return True

    def login(self, password):
        return password == self.password

if __name__ == "__main__":
    usuario = Usuario("pablo", "phschwarzenberg@uc.cl")
    print(usuario.cambiar_password("clave"))
    print(usuario.cambiar_password("clavesecreta1_"))
    print(usuario.cambiar_password("clavesecreta"))
    print(usuario.cambiar_password("clasesecreta1"))
    print(usuario.cambiar_password("claveSecreta1"))
    print(usuario.login("clavesecreta1_"))
    print(usuario.login("claveSecreta1"))

           