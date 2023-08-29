class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.password = ""

    def cambiar_password(self, password):
        if len(password) > 16:
            return False
        if len(password) < 8:
            return False
        a=0
        for letra in password:
            if letra.isnumeric():
                a = a+1
        if a == 0:
            return False
        c = 0
        for letra in password:
            if letra.isupper():
                c = c+1
            if letra == "_":
                c = c+1
        if c == 0:
            return False

        else:
            return True
        pass

    def login(self, password):
        if self.password == password:
            return True
        else:
            return False
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
           