class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.password = ""

    def cambiar_password(self, password):
        abc=""
        for i in range(97, 123):
            abc += chr(i)
        digitos=""
        for i in range(10):
            digitos+=str(i)
        if len(password) >= 8 and len(password) <= 16:
            cont_letras=0
            cont_digitos=0
            for caracter in password:
                if caracter in abc:
                    cont_letras+=1
                if caracter in digitos:
                    cont_digitos+=1
            if cont_digitos+cont_letras!=len(password):
                self.password=password
                return True
            else:
                return False
        else:
            return False
    def login(self, password):
        if self.password==password:
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
           