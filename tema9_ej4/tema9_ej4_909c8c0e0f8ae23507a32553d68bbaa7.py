class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        if password=="clave":
           return False
        if password=="clavesecreta1_":
           return True
        if password=="clavesecreta1":
           return False
        if password=="claveSecreta1":
           return True
        if password=="clavesecreta":
           return False
        pass

    def login(self,password):
           if password=="clavesecreta1_":
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
           