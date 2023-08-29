class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        numero = False
        lena = False
        especial = False
        letra = False
        for i in password:
   
          if i in "124567890":
            numero = True
          if i in "abcdefghijklmnopqrstvwxyz":
            letra = True
          if i in "_#" or i.isupper():
            especial = True
        if len(password) >= 8 and len(password) <= 16:
          lena = True
        if lena and numero and especial and letra:
        
          self.password = password
          return True
        else:
          return False
    def login(self,password):
        if password == self.password:
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
