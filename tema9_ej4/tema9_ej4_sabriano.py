import string
class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""
    def cambiar_password(self,password):
        numeros=[1,2,3,4,5,6,7,8,9,0]
        mayusculas=string.ascii_uppercase
        caracteres=["_","#","$","%","*","-"]
        contador=1
        if len(password)<8 or len(password)>16:
            return False
        else:
            lista=list(password)
            for i in lista:
                if i in numeros:
                    contador=contador+1
                if i in mayusculas:
                    contador=contador+1
                if i in caracteres:
                  contador=contador+1
        if contador==2 or contador>2:
            self.password=password
            return True
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
           