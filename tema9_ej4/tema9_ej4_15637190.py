class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        l=len(password)
        if 8<=l<=16:
            if str.isnumeric(password)==False:
                if str.isalpha(password)==False:
                    if str.islower(password)==False or str.isalnum(password)==False:
                        self.password=password
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
                        
                        
                        
        else:
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
           