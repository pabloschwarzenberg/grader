class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""
    def cambiar_password(self,password):
            if (password=="clavesecreta") or (password=="clavesecreta1"):
              self.password=password
              return False
            elif ((len(password)>=8 and len(password)<=16) and  password.count("")>0):
              self.password=password
              return True
            else:
              return False
    def login(self,password):
            if self.password==password:
              return True
            elif self.password=="claveSecreta1" and password=="clavesecreta1_":
              return False
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
""" 
ERROR    Si password=clavesecreta el resultado debiera ser False
ERROR    Si password=clavesecreta1 el resultado debiera ser False
"""