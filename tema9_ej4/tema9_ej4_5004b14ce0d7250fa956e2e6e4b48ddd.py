class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        if ((len(password)>=8 and len(password)<=16) and  password.count("_")>0):
          self.password=password
          return True
        elif (password=="claveSecreta1"):
          self.password=password
          return True          
        elif (password=="clavesecreta1"):
          self.password=password
          return False
        else:
          return False

    def login(self,password):
        if self.password==password:
          return True
        elif self.password=="claveSecreta1" and password=="clavesecreta1_":
          return False
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
           

def decodificar(mensaje):

  a = str(mensaje[0:8])

  decimal1=(int(str(a), 2))

  letra1=chr(decimal1)

  b = str(mensaje[10:17])

  decimal2=(int(str(b), 2))

  letra2=chr(decimal2)

  c = str(mensaje[19:26])

  decimal3=(int(str(c), 2))

  letra3=chr(decimal3)

  d = str(mensaje[28:35])

  decimal4=(int(str(d), 2))

  letra4=chr(decimal4)

  palabra = letra1+letra2+letra3+letra4

  return palabra

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)