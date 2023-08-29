class Usuario:
    def __init__(self,nombre,email):
        self.nombre = nombre
        self.email = email
        self.password = ""

    def cambiar_password(self,password):
        a = "abcdefghijklmnñopqrstuvwxyz"
        b = a.upper()
        c = 0
        d = 0
        e = 0
        f = 0
        for i in password:
            if i.isdigit() ==  True:
                c = c + 1
            elif i in a:
                d = d + 1
            elif i in b:
                f = f + 1
            elif i.isalpha() == False and i.isdigit() == False:
                e = e + 1
        if (e != 0 or f != 0) and d != 0 and c != 0:
            return True
        else:
            return False


    def login(self,password):
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
           