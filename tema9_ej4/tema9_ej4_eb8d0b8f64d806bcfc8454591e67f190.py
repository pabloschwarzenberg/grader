class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        if len(password)>=8 and len(password)<=16:
            contador=0
            contador2=0
            for i in password:
                if i.isalnum():
                    contador=contador+1
                if i.isupper():
                    contador2=contador2+1
            if contador2>0 or len(password)-contador>0:
                self.password=password
                return True
            else:
                return False
        else:
            return False    
        pass

    def login(self,password):
        if self.password==password:
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
           