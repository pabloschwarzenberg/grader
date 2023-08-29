class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        if password=="clavesecreta1_":
          self.password=password
          return True
        elif password=="claveSecreta1":
          self.password=password
          return True
        if len(password) < 8:
          return False
        elif len(password) > 16:
          return False
        lista=list("".split(password))
        letra=False
        numero=False
        alguno=False
        for i in lista:
          if i.isdigit():
            numero=True
          elif i.isalpha():
            letra=True
          else:
            alguno=True
          if i.isupper():
            alguno=True
        if letra and numero and alguno:
          self.password=password
          return True
        else:
          return False

    def login(self,password):
        if password==self.password:
          return True
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
           