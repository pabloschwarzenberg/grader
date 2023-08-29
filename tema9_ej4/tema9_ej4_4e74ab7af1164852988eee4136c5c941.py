class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.password = ""

    def cambiar_password(self, password):
        self.password = password

    def login(self, password):
        if self.password == password:
            return True
        else:
            return False

if __name__ == "__main__":
    usuario = Usuario("pablo", "phschwarzenberg@uc.cl")
    print(usuario.login("clave"))
    print(usuario.login("clavesecreta1_"))
    print(usuario.login("clavesecreta"))
    print(usuario.login("clavesecreta1"))
    print(usuario.login("claveSecreta1"))

    usuario.cambiar_password("clavesecreta1_")
    print(usuario.login("clavesecreta1_"))
    print(usuario.login("claveSecreta1"))
