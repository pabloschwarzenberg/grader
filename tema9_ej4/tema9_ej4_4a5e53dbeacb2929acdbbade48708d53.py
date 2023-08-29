class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""
    def cambiar_password(self,password):
        h=0
        g=0
        d=0
        if(8<=len(password)<=16):
            for a in password:
                if(47<ord(a)<58):
                    d=1
                    
                if(96<ord(a)<123):
                    h=1
                    
                if(32<ord(a)<=47 or 58<=ord(a)<=96 or 123<=ord(a)):
                    g=1
                    
            if(h==1 and g==1 and d==1):
                self.password=password
                return(True)
            else:
                return(False)
        else:
            return False
    def login(self,password):
         if(password==self.password):
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
           