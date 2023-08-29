def buscarletra(clave):
  abecedario=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
  for i in abecedario:
    if clave.find(i)>-1:
      return True
  return False
def buscarnumero(clave):
  numeros=["1","2","3","4","5","6","7","8","9"]
  for i in numeros:
    if clave.find(i)>-1:
      return True
  return False
def mayuscula(clave):
  x=list(clave)
  for i in x:
    if 64<ord(i)<91 :
      return True
  return False
def simbolo(clave):
  x=list(clave)
  for i in x:
    if 32<ord(i)<48 or 90<ord(i)<97 or 122<ord(i)<255:
      return True
  return False

class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        if 7<len(password)<17 and buscarletra(password)==True and buscarnumero(password)==True and (mayuscula(password)==True or simbolo(password)==True):
           self.password=password
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
           