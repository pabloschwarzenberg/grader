class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.password = ""

    def cambiar_password(self, password):
        self.password=password
        abecedario="abcdefghijklmnopqrstuvwxyz"
        ABECEDARIO="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        c=0
        d=0
        e=0
        if 8<=len(password)<=16:
            for i in password:
                if i in abecedario:
                    c=c
                    d=1
                elif i in ABECEDARIO:
                    c=c
                    e=1
                else:
                    c+=1
            c=c+d+e
            if c>=3:
                r=True
                self.password=password
            else:
                r=False
                password=""
        else:
            r=False
            password=""
        return r

    def login(self, password):
        if password==self.password:
            r=True
        else:
            r=False
        return r


if __name__ == "__main__":
    usuario = Usuario("pablo", "phschwarzenberg@uc.cl")
    print(usuario.cambiar_password("clave"))
    print(usuario.cambiar_password("clavesecreta1_"))
    print(usuario.cambiar_password("clavesecreta"))
    print(usuario.cambiar_password("clasesecreta1"))
    print(usuario.cambiar_password("claveSecreta1"))
    print(usuario.login("clavesecreta1_"))
    print(usuario.login("claveSecreta1"))
