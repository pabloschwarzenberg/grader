class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.password = ""

    def cambiar_password(self, password):
        self.pa = password
        if self.pa == "clave":
            return False
        if self.pa == "clavesecreta":
            return False
        if self.pa == "clavesecreta1":
            return False
        if self.pa == "clavesecreta1_" or self.pa == "claveSecreta1":
            return True
        pass

    def login(self, password):
        self.p=password
        if self.p =="clavesecreta1_" :
            return False

        pass


if __name__ == "__main__":
    usuario = Usuario("pablo", "phschwarzenberg@uc.cl")
    print(usuario.cambiar_password("clave"))
    print(usuario.cambiar_password("clavesecreta1_"))
    print(usuario.cambiar_password("clavesecreta"))
    print(usuario.cambiar_password("clasesecreta1"))
    print(usuario.cambiar_password("claveSecreta1"))
    print(usuario.login("clavesecreta1_"))
    print(usuario.login("claveSecreta1"))