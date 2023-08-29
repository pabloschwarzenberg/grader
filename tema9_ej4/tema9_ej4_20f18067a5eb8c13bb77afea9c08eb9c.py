class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        if len(password)>=8 and len(password)<=16:
            if password.isalpha()!=True and password.isdigit()!=True:
                import string
                for i in list(string.ascii_uppercase):
                    if password.find('{0}'.format(i))>=0 or password.find('_')>=0:
                        self.password=password
                        return True
                    elif i=='Z' and password.find('{0}'.format(i))==-1:
                        return False
                    else:
                        continue
            elif password.isalpha()==True or password.isdigit()==True:
                return False
            
        else:
            return False
            
    def login(self,password):
        if password==self.password:
            return True
        elif password!=self.password:
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
           