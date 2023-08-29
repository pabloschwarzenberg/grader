class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.password = ""

    def cambiar_password(self, password):
        x=1
        c=1
        y=1
        if 8<=len(password)<=16:
            for i in password:
                if i.isdigit():
                  x=2
                if i.isupper():
                    c=2
                if not i.isalnum():
                    y=2
            if x==2 and (c==2 or y==2):
                self.password=password
                return True
            else:
                return False
        else:
            return False



    def login(self, password):
        if self.password == password:
            return True
        else:
            return False

if __name__ == "__main__":
    usuario=Usuario("pablo","phschwarzenberg@uc.cl")
    print(usuario.cambiar_password("clave"))
    print(usuario.cambiar_password("clavesecreta1_"))
    print(usuario.cambiar_password("clavesecreta"))
    print(usuario.cambiar_password("clasesecreta1"))
    print(usuario.cambiar_password("claveSecreta1"))
    print(usuario.login("clavesecreta1_"))
    print(usuario.login("claveSecreta1"))