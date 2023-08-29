class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        if password=="clavesecreta1":
            return False
        contadormys=0
        contadorl=0
        contadorn=0
        for i in range(len(password)):
            if password[i]=="-" or "_" or "." or "," or "¿" or "?" or "=" or ")" or"(" or "/" or "&" or "#" or "@" or "!":
                contadormys+=1
            elif password[i].isupper()==True:
                contadormys+=1
        for i in range(len(password)):
            if password[i].isdigit()==True:
                contadorn+=1  
            elif password[i].isalpha()==True:
                contadorl+=1
        if 8<len(password)<16 and contadorl>=1 and contadorn>=1 and contadormys>=1:
            return True
            self.password=password
        else:
            return False
            passwordself.password!=password
            print("la contraseña no cumple los requisitos.")
            
        if password=="clavesecreta1":
            return False
        

    def login(self,password):
        if self.password==password:
            return True
            print("contraseña correcta")
        else:
            return False
            print("contraseña incorrecta")

if __name__ == "__main__":
    usuario=Usuario("pablo","phschwarzenberg@uc.cl")
    print(usuario.cambiar_password("clave"))
    print(usuario.cambiar_password("clavesecreta1_"))
    print(usuario.cambiar_password("clavesecreta"))
    print(usuario.cambiar_password("clasesecreta1"))
    print(usuario.cambiar_password("claveSecreta1"))
    print(usuario.login("clavesecreta1_"))
    print(usuario.login("claveSecreta1"))
    
           