class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        if (8<=len(password)<=16)==True:
            if password.isalpha()==False:
                for i in password:
                    if i.isdigit()==True:
                        for k in password:
                            if k.isalnum()==False or k.isupper():
                                self.password=password
                                return True
                        else:
                            return(False)
                else:
                    return(False)
            else:
                return(False)
        else:
            return(False)

    def login(self,password):
        if password==self.password:
            return True
        else:
            return False
        

if __name__ == "__main__":
    usuario=Usuario("pablo","phschwarzenberg@uc.cl")
    print(usuario.cambiar_password("clave"))
    print(usuario.cambiar_password("clavesecreta_1"))
    print(usuario.cambiar_password("clasesecreta1"))
    print(usuario.cambiar_password("claveSecreta1"))
    print(usuario.login("clavesecreta1"))
    print(usuario.login("claveSecreta1"))
  

  
          