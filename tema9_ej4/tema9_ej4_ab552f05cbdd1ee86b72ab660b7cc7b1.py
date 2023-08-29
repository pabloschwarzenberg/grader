class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        if len(password)<=16 and len(password)>=8:
          i=0
          j=0
          contador=0
          contador2=0
          while contador <=len(password)-1:
            if numeros.find(password[contador])!=-1:
                i=i+1
            contador=contador+1
          while contador2 <=len(password)-1:
            if alfabeto.find(password[contador2])!=-1:
                j=j+1
            contador2=contador2+1
          if i>0 and j>0 and (i+j)<len(password):
            self.password=password
            return True
          else:
            return False
        else:
          return False
                

    def login(self,password):
        if password==self.password:
            return True
        else:
            return False
numeros="0123456789"
alfabeto="abcdefghijklmnñopqrstuvwxyz"

if __name__ == "__main__":
    usuario=Usuario("pablo","phschwarzenberg@uc.cl")
    print(usuario.cambiar_password("clave"))
    print(usuario.cambiar_password("clavesecreta1_"))
    print(usuario.cambiar_password("clavesecreta"))
    print(usuario.cambiar_password("clasesecreta1"))
    print(usuario.cambiar_password("claveSecreta1"))
    print(usuario.login("clavesecreta1_"))
    print(usuario.login("claveSecreta1"))