class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
      alfanumerico= False
      Numero= False
      especial= False
      for l in range(len(password)):
        if password[l].isalpha():
          alfanumerico= True
        if password[l].isnumeric():
          Numero= True
        if not password[l].isalpha() and not password[l].isnumeric():
          especial= True
        if password[l].isupper():
          especial=True

      if len(password)>=8 and len(password)<=24 and alfanumerico and Numero and especial:
          self.password= password
          return True
      else:
        return False

    def login(self,password):
      self.claveintento= password
      if self.claveintento == self.password:
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