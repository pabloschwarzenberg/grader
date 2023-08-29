class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        abc = 'abcdefghijklmnopqrstuvwxyz'
        num = '0123456789'
        car = '°|¬!"#$%&/()=?\'\\¿¡+*~´¨{[^}]`,;.:-_<>'
        p = 0
        for i in abc:
            if i in password:
                p += 1
                break
        for i in num:
            if i in password:
                p += 1
                break
        for i in car:
            for j in abc:
                if j.upper() in password or i in password:
                    p += 1
                    break
            if p == 3:
                break
        if p == 3:
            self.password = password
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
           