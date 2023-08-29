class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        cs="+#%&!?¡¿_-"
        if len(password)>7 and len(password)<17:
            for i in password:
                if i.isdigit():
                    for i in password:
                        if i.isalpha:
                            for i in password:
                                if i.isupper() or i in cs:
                                    self.password=password
                                    return True

        return False                 
            
                
            

    def login(self,password):
        if password==self.password:
            return True
        return False
        






if __name__ == "__main__":
    usuario=Usuario("pablo","phschwarzenberg@uc.cl")
    print(usuario.cambiar_password("clave"))
    print(usuario.cambiar_password("clavesecreta1_"))
    print(usuario.password)
    print(usuario.cambiar_password("clavesecreta"))
    print(usuario.cambiar_password("clasesecreta1"))
    print(usuario.cambiar_password("claveSecreta1"))
    print(usuario.password)
    print(usuario.login("clavesecreta1_"))
    print(usuario.login("claveSecreta1"))

           


           