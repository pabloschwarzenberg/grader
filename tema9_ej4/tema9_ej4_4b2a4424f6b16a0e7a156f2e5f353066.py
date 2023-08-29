class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        self.password = password
        if len(password)>=8 and len(password)<=16:
            #print('1st')
            if password.isalpha() == False:
                 #print('2nd')
                if password.islower() == False or password.isalnum() == False:
                    #print('3rd')
                    return True
                else:
                    return False
            else:
                return False        
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
    print('\n')
    print(usuario.login("clavesecreta1_"))
    print(usuario.login("claveSecreta1"))
           