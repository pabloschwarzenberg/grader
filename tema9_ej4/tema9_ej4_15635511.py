__author__ = 'Nicolas'
class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        if 8<=len(password)<=16:
          numeros=["0","1","2","3","4","5","6","7","8","9"]
          letras=["a","b","c","d","e","f","g","h","i","j","k","l","m","ñ","n","o","p","q","r","s","t","u","v","w","x","y","z"]
          c=list(map(lambda x: x.upper(),letras))
          signo=["#","_","-"]
          contador_min=0
          contador_may=0
          contador_sig=0
          contador_num=0
          for i in range (len(password)):
              if password[i] in numeros:
                  contador_num+=1
              if password[i] in letras:
                  contador_min+=1
              if password[i] in c:
                  contador_may+=1
              if password[i] in signo:
                  contador_sig+=1
          contador_letras=contador_may+contador_min
          if contador_letras>=1 and contador_num>=1 and (contador_may>=1 or contador_sig>=1):
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

if __name__ == "__main__":
    usuario=Usuario("pablo","phschwarzenberg@uc.cl")
    print(usuario.cambiar_password("clave"))
    print(usuario.cambiar_password("clavesecreta1_"))
    print(usuario.cambiar_password("clavesecreta"))
    print(usuario.cambiar_password("clasesecreta1"))
    print(usuario.cambiar_password("claveSecreta1"))
    print(usuario.login("clavesecreta1_"))
    print(usuario.login("claveSecreta1"))
           