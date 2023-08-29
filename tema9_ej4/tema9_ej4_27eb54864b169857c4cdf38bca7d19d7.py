class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
      a = 0
      d = 0
      z = 0
      for p in password:
          if p.isdigit() == True:
            d += 1
          elif p.isalpha() == True:
            a += 1
          else:
            z += 1
            
      if len(str(password)) > 7 and len(str(password)) < 17 and a != 0 and d != 0:
        if z != 0:
          self.password = password
          return True
        elif z == 0:
          for p in password:
            if p != p.lower():
              self.password = password
              return True
            if password == password.lower():
              return False
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
           