import re
class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        mayusculas=re.sub('[^A-Z]', '', password)
        minusculas=re.sub('[^a-z]', '', password)
        numeros=re.sub('[^\d]', '', password)
        if len(minusculas)==0 or len(numeros)==0 or len(password)<8 or len(password)>16:
            return False
        
        x=len(password)-len(numeros)-len(minusculas)-len(mayusculas)
        if len(mayusculas)==0 and x==0:
            return False
        elif len(mayusculas)!= 0 or x!=0:
            self.password=password
            return True
    
    def login(self,password):
        if password==str(self.password):
            return True
        else:
            return False
        pass

if __name__ == "__main__":
    x=len(password)-numeros-minusculas-mayusculas
    mayusculas=re.sub('[^A-Z]', '', password)
    minusculas=re.sub('[^a-z]', '', password)
    numeros=re.sub('[^\d]', '', password)
    usuario=Usuario("pablo","phschwarzenberg@uc.cl")
    print(usuario.cambiar_password("clave"))
    print(usuario.cambiar_password("clavesecreta1_"))
    print(usuario.cambiar_password("clavesecreta"))
    print(usuario.cambiar_password("clasesecreta1"))
    print(usuario.cambiar_password("claveSecreta1"))
    print(usuario.login("clavesecreta1_"))
    print(usuario.login("claveSecreta1"))
           
           