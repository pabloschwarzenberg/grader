class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWYXZ"
        minusculas = "abcdefghijklmnopqrstuvwxyz"
        numeros = "1234567890"
        simbolos = "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~" 
        self.password=password
        if len(self.password)>=8 and len(self.password)<=16:
            for i in self.password:
                if i in numeros:
                    if i in mayusculas or i in simbolos:
                        return True
                    else:
                        return False       
                else:
                    return False
        else:
            return False
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