class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        ABC = list(ABC)
        abc = "abcdefghijklmnopqrstuvwxyz"
        abc = list(abc)
        numeros = "1234567890"
        numeros = list(numeros)
        if (len(password)>=8) and (len(password)<=16):
          password=list(password)
          cont=0
          cond1=0
          cond2=0
          cond3=0
          for i in password:
            if i in ABC:
              cont+=1
              cond1+=1
            elif i in abc:
              cont+=1
            elif i in numeros:
              cont+=1
              cond2+=1
            else:
              cond3+=1
          if (cond2>0) and ((cond1>0) or (cond3>0)):
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
           