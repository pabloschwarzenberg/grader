class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        lista=["_",",","="]
        if len(password)>=8 and len(password)<=16:
            for i in password:
                for j in password.upper():
                    if i==j or (i in lista):
                        for l in password:
                            for k in range(10):
                                if l==str(k):
                                    self.password=password
                                    return True
                                elif password[-1:]==l and l!=k and k==9:
                                    return False
                    elif password[-1:]==i and (i not in lista):
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
           