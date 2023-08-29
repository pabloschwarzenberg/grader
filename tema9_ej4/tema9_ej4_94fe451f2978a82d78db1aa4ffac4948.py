class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        c_especial = False
        c_num = False
        c_mayus = False

        for i in password:
            if i.isalpha()==False and i.isdigit()==False:
                c_especial = True
            elif i.isalpha()==False and i.isdigit()==True:
                c_num = True
            
            if i.isupper():
                c_mayus = True

        if len(password)>=8 and len(password)<=16 and c_num==True and  (c_mayus==True or c_especial==True):
            self.password = password
            return True
        else:
            return False

    def login(self,password):
        if password==self.password:
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
           