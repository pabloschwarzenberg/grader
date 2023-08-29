class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        letra=False
        numero=False
        mayuscula=False
        minuscula=False
        especial=False
        if(len(password)<8 or len(password)>16):
            self.password=""
            return(False)
        for i in password:
            if (i.isalpha() ):
                letra=True
            if (i.isnumeric()):
                numero=True
            if (i.isupper()):
                mayuscula=True
            if (i.lower()):
                minuscula=True
            if ( i.isalpha()==False and i!="#" and i.isnumeric()==False):
                especial=True
        
        if( (numero and minuscula and letra) and (mayuscula or especial) ):
            return(True)
            self.password=password
        else:
            self.password=""
            return(False)

    def login(self,password):
        if(password == self.password):
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
           