class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.password = ""

    def cambiar_password(self, password):
        x = len(password)
        caracteres = ["!", "@", "#", "$", "%", "^", "&", "*", "_", "-"]
        if 7 < x < 17:
            my = 0
            n = 0
            c = 0
            for letra in password:
                i = 0
                while i < len(caracteres):
                    if caracteres[i] == letra:
                        c = 1
                    i = i + 1
                if letra.isupper():
                    my = 1
                if letra.isdigit():
                    n = 1
            if n != 0 and (my != 0 or c != 0):
                self.password = password
                return True
            else:
                return False
        else:
            return False

    def login(self, password):
        if password == self.password:
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
