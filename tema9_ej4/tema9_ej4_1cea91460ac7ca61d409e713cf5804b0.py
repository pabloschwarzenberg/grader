def numero(string):
  return any(i.isdigit() for i in string)
def caracteres(string):
    letras_mayus="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letras_min="abcdefghijklmnopqrstuvwxyz"
    numeros="1234567890"
    for i in string:
      if i not in letras_mayus and i not in letras_min and i not in numeros: return "especial"
      elif i in letras_mayus: return "mayuscula"
        
class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""


    def cambiar_password(self,password):
        if 8<=len(password)<=16 and numero(password) and (caracteres(password)=="especial" or caracteres(password)=="mayuscula"):
          self.password=password
          return True
        else: return False

    def login(self,password):
        if password==self.password: return True
        else: return False

if __name__ == "__main__":
    usuario=Usuario("pablo","phschwarzenberg@uc.cl")
    print(usuario.cambiar_password("clave"))
    print(usuario.cambiar_password("clavesecreta1_"))
    print(usuario.cambiar_password("clavesecreta"))
    print(usuario.cambiar_password("clasesecreta1"))
    print(usuario.cambiar_password("claveSecreta1"))
    print(usuario.login("clavesecreta1_"))
    print(usuario.login("claveSecreta1"))
    print(caracteres("clavesecreta1_"))
    

      