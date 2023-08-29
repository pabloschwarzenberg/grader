

class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        if len(password)<8:
            return False
        if len(password)>16:
            return False
        if password!=password.lower():
            self.password=password
            return True
        caracteres=[",","!","#","$","%","&","/","?","í","[","]","-","_"]
        for i in range(len(caracteres)):
            if caracteres[i] in password:
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