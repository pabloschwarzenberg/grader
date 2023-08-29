class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        contador=0
        simbolos=["_","%","$","&","/","!","#"]
        if 8<=len(password)<=16:
            if password.isalnum()==False:
                for sim in simbolos:
                    if sim in password:
                        self.password=password
                        return True
                    else:
                        return False
            elif password.isalnum()==True:
                for i in password:
                    if i.isupper()==True:
                        contador+=1
                if contador>0:
                    self.password=password
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    def login(self,password):
        conjunto=[self.nombre,self.password]
        if password in conjunto:
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
           