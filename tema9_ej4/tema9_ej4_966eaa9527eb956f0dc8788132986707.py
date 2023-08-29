class Usuario:

    def __init__(self,user,mail):
        self.user = user
        self.clave = ''
        self.mail = mail

    def cambiar_password(self,password):
        l = len(password)
        cond = 0
        for c in password:
            print(c)
            print(cond)
            if (c.istitle() is True) or (password.isalnum() is False):
                cond = 1
                print(cond)
                break
        if 8 < l < 16 and cond == 1:
            self.clave = password
            return True
        else:
            return False

    def login(self, password):
        if self.clave == password:
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
           