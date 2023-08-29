class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
      a = False
      b = False
      global a
      global b
      if len(password)<=16 and len(password)>=8:
        for char in password:
          if char.isupper()== True or char=="_":
            a = True
          if char.isdigit()== True:
            b = True
        if a ==True and b==True:
            self.password = password
        else:
          return False
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
           