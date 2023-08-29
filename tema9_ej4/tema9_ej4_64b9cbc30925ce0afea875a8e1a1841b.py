class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        if len(password)<=8:
          return False
        elif len(password)>=16:
            return False
        else:
            n = 0
            l = 0
            m = 0
            minu = 0
            o = 0
            for i in password:
                if i.isdigit():
                    n = n + 1
                elif i.islower():
                    minu = minu + 1
                elif i.isupper():
                    m = m + 1
                elif i.isspace():
                    pass
                else:
                    o = o + 1
            if m>=1 or o>=1:
                self.password = password
                return True
            else:
                return False
            
    def login(self, password):
        if self.password == Usuario.cambiar_password:
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