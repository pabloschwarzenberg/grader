import string as s

def isspecial(x):
    x = list(x)
    for signo in s.punctuation:
        if signo in x:
            return True
    return False

class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self, password):
        if isinstance(password, str) and 8 <= len(password) <= 16 and password.isalpha() == False:
          if password.islower() == False or isspecial(password) == True:
            self.password = password
            return True
          else:
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
           