class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        if len(password) >= 8 and len(password) <= 16:
          if password.isalpha() == False:
            if password.isdigit() == False:
              for i in range(0, len(password)):
                if ord(password[i]) > 32 and ord(password[i]) < 48:
                  self.password = password
                  return True
                if ord(password[i]) > 57 and ord(password[i]) < 97:
                  self.password = password
                  return True
          return False
        else:
            return False

    def login(self,password):
        if password == self.password:
          return True
        if password != self.password:
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