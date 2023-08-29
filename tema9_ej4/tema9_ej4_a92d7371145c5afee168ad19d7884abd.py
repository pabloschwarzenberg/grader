class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        a=None
        b=None
        c=None
        d=None
        if len(password) >=8 and len(password) <=16:
            a = True
        for i in password:
            if i.isalpha()== True:
                b= True
            if i.isnumeric()==True:
                c= True
            if i.isupper() == True or i.isalnum()==False:
                d= True    
        if a== True and b== True and c==True and d==True:
            self.password=password
            return True
        else:
            return False
        

    def login(self,password):
        if password == self.password:
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
