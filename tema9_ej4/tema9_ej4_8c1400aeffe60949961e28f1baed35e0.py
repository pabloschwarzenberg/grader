class Usuario:
    def __init__(self,nombre,email):
        self.nombre=str(nombre)
        self.email=str(email)
        self.password=""

    def cambiar_password(self,password):
        for i in self.password:
                
            if self.password.isalnum()==True and 8<=len(self.password)<=16 and self.password[i].isupper()==True and self.password[i].isalnum()==False:
                self.password=password
                return True
            else:
                return False


    def login(self,password):
        if cambiar_password==True:
            
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
           