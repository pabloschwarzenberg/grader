import re
class usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""



    def cambiar_password(self,password):
        m="[A-Z]"
        i="[^A-Za-z1-9]"
        if (8<= len(password)<=16) and (re.search(m,password)) or (re.search(i,password)):
            self.password=password
            return True
        else:
            return True

         else:
             return False


    def __name__=="__main__":
        usuario=usuario("pablo","phschwarzenbergQuc,cl"")
        print(usuario.cambiar_password("clave"))
        print(usuario.cambiar_password(clave1_=))
        print(usuario.cambiar_password("clave"))
        print(usuario.cambiar_password("clave1"))
        print(usuario.cambiar_password("clave1"))
        print(usuario.login("clave1_"))
        print(usuario.login("clave1"))