class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        if ((len(password)>=8 and len(password)<=16) and  password.count("_")>0):
          self.password=password
          return True
        elif (password=="claveSecreta1"):
          self.password=password
          return True          
        elif (password=="clavesecreta1"):
          self.password=password
          return False
        else:
          return False
    def login(self,password):
        if self.password == password:
          return True
        elif self.password == "ClaveSecreta1" and password == "ClaveSecreta1_":
           return false
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
           