import re
class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        mayus = re.sub('[^A-Z]', '', password)
        minus = re.sub('[^a-z]', '', password)
        nums = re.sub('[^\d]', '', password)
        especiales = re.sub('[A-Za-z\d\s]','', password)
        if len(password)>=8 and len(password)<=16 and len(minus)>0 and len(nums)>0 and (len(mayus)>0 or len(especiales)>0):
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
           