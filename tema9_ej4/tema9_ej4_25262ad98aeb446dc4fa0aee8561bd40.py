class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.password = ""

    def cambiar_password(self, password):
        validador = [False, False, False]

        if len(password) >= 8 and len(password) <= 16:

            for i in password:
                if i.isnumeric():
                    validador[0] = True
                elif i.isalpha():
                    validador[1] = True
                else:
                    validador[2] = True

                if i.isupper():
                    validador[2] = True

        if False in validador:
            self.password = False
            return False
        else:
            self.password = password
            return True

    def login(self, pw):
        if self.password == pw:
            return True
        else:
            return False


if __name__ == "__main__":
    usuario = Usuario("pablo", "phschwarzenberg@uc.cl")
    print(usuario.cambiar_password("clave"))
    print(usuario.cambiar_password("clavesecreta1_"))
    print(usuario.cambiar_password("clavesecreta"))
    print(usuario.cambiar_password("clasesecreta1"))
    print(usuario.cambiar_password("claveSecreta1"))
    print(usuario.login("clavesecreta1_"))
    print(usuario.login("claveSecreta1"))
