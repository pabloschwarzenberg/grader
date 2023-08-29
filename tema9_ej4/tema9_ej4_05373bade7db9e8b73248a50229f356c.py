class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        if 16>=len(password)>=8:
          if password.isalpha()==False and password.isdigit()==False:
            if password!=password.lower() or password.isalnum()==False:
              self.password=password
              return True
            else:
              return False
          else:
            return False
        else:
          return False
                  

    def login(self,password):
        if self.password==password:
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
           