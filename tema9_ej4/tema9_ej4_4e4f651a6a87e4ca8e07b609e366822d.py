class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        if len(password)>=8 and len(password)<=16:
            M=0
            if password.isalnum()==True:
                for i in password:
                    if i.isupper()==True:
                        M=1
                    else:
                        pass
            if password.isalnum()==False:
                for i in password:
                    if i.isalnum()==False:
                        M=1
                    else:
                        pass
        if len(password)<8 or len(password)>16:
            return False

        if M==1:
                self.password=password
                return True
        if M==0:
                return False
    def login(self,password):
        if password==self.password:
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
           