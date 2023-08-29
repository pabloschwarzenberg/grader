from string import  punctuation
class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        if 17>len(password)>7:
            if any([c.isdigit() for c in password])==True:
                if any([c.islower() for c in password])==True:
                    if any([c.isupper() for c in password]) == True or any([True if c in punctuation else False for c in password]):
                            self.password=password
                            return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    def login(self,password):
        if self.password==password:
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
           