class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
      p = list(password)
      c = 0
      d = 0
      for a in p:
        b = ord(a)
        if b>=65 and b<=90:
          c += 1
        elif (b>=33 and b<=47) or (b>=58 and b<=64) or (b>=91 and b<=96) or (b>=123 and b<=126):
          d += 1

      if (len(password)>=8 and len(password)<=16) and (password.isalpha()==False) and (c>0 or d>0):
        self.password = password
        return True
      else:
        return False

    def login(self,password):
      if password==self.password:
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
           