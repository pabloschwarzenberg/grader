import re
class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        mayus=r"[A-Z]"
        isnt=r"[^A-Za-z1-9]"
        if (8 <= len(password) <= 16) and (re.search(mayus, password) or re.search(isnt,password)):
            self.password=password
            return True
        else:
            return False

    def login(self,password):
        if password is self.password:
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
           