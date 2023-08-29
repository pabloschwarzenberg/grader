import re
class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        g=r"[A-Z]"
        t=r"[^A-Za-z1-9]"
        if ((re.search(t,password)) or (re.search(g,password))) and (8<=len(password)<=16):
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

