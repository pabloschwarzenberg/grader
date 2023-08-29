class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        p=password.split()
        n=0
        m=0
        q=0
        r=0
        for a in p:
            if a.isdigit()==True:
                n=1
        for a in p:
            if a.isalpha()==True:
                m=1
        for a in p:
            if a.isupper()==True:
                q=1
        for a in p:
            if a.isalnum()==False:
                r=1
        
        
                
        if len(password)<8:
            return False
        elif len(password)>16:
            return False
        elif m==0:
            return False
        else:
            return True

        
        
        
                


        
            

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
           