class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,newpassword):
        if 7 < len(newpassword) < 17 and (not(newpassword.isalnum()) or newpassword != newpassword.lower()):
          self.password = newpassword
          return True
        else:
          return False
        pass

    def login(self,password):
        if self.password == password:
          return True
        else:
          return False
        pass

if __name__ == "__main__":
    usuario=Usuario("pablo","phschwarzenberg@uc.cl")
    print(usuario.cambiar_password("clave"))
    print(usuario.cambiar_password("clavesecreta1_"))
    print(usuario.cambiar_password("clavesecreta"))
    print(usuario.cambiar_password("clasesecreta1"))
    print(usuario.cambiar_password("claveSecreta1"))
    print(usuario.login("clavesecreta1_"))
    print(usuario.login("clavesecreta1"))
           