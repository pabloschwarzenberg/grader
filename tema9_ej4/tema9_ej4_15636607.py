class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        l=len(password)
        cu=0
        can=0
        ca=0
        cn=0
        if l<8 or l>16:
            return False
        else:
            for i in range(0,l):
                if password[i].isupper()==True:
                    cu=cu+1
                if password[i].isalnum()==False:
                    can=can+1
                if password[i].isalpha()==True:
                    ca=ca+1
                if password[i].isnumeric()==True:
                    cn=cn+1
        if (cu>0 or can>0) and ca>0 and cn>0:
            self.password=password
            return True
        else:
            return False
        pass

    def login(self,password):
        if password==self.password:
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
           