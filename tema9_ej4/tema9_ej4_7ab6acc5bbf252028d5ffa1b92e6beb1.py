import re
class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        numeros=re.compile("\d")
        letras=re.compile("[a-z]{3,}")
        letra_mayuscula=re.compile("[A-Z]")
        simbolos=re.compile("_")
        if 8<=len(password)<=16 and letras.search(password)!=None and numeros.search(password)!=None and (letra_mayuscula.search(password)!=None or simbolos.search(password)!=None):

            self.password=password
            return True
        else:
            self.password=self.password
            return False
        pass

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
           