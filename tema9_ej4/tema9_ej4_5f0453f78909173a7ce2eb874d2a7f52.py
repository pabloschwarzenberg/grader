def Numb(inputS):
  return any(char.isdigit() for char in inputS)
def Mayus(inputS):
  return any(char.isupper() for char in inputS)
def Esp(inputS):
  return any(char.isalpha() for char in inputS)
class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
          if len(password)<17 and len(password)>7 and Numb(password)==True and (Mayus(password)==True or password.isalnum()==False):
            self.password=password
            return True
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
           