class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        num = 0
        letra = 0
        especial = 0
        for caracter in password:
          if caracter.isnumeric():
            num = 1
          else:
            if caracter not in "abcdefghijklmnopqrstuvwxyz":
              especial = 1
            else:
              letra = 1
        if 8<=len(password)<=16 and num == 1 and letra == 1 and especial == 1:
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
           