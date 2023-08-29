class Usuario:
    def init(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        if password=="clavesecreta1" or password=="claveSecreta1":
          return True
        else:
          return False

    def login(self,password):
        if password=="clavesecreta1" or password=="claveSecreta1":
          return True
        else:
          return False

if __name__ == "__main__":
    usuario=Usuario("pablo","phschwarzenberg@uc.cl")
    print(usuario.cambiar_password("clave"))
    print(usuario.cambiarpassword("clavesecreta1"))
    print(usuario.cambiar_password("clavesecreta"))
    print(usuario.cambiar_password("clasesecreta1"))
    print(usuario.cambiarpassword("claveSecreta1"))
    print(usuario.login("clavesecreta1"))
    print(usuario.login("claveSecreta1"))
           