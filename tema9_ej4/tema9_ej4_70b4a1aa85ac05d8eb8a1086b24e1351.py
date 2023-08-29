class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        l, p, d = 0, 0, 0
        if (len(password) > 7 or len(password) < 17):
            for i in password:        
                if (i.islower()):
                    l+=1                                      
                if (i.isdigit()):
                    d+=1                    
                if (i.isupper()) or (i=='@'or i=='$' or i=='_'):
                    p+=1           
        if (l>=1 and p>=1 and d>=1 and l+p+d==len(password)):
            self.password = password
            return True
        else:
            return False

    def login(self,password):
        if self.password == password:
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
           