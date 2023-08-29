class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        a=0
        b=0
        c=0
        d=0
        numero="1234567890"
        abcedario="abcdefghijklmnopqrstuvwxyz"
        tr=abcedario.upper()
        for i in password:
          
          if abcedario.find(i)!=-1:
            a+=1
          elif numero.find(i)!=-1:
            b+=1
          elif tr.find(i)!=-1:
            d+=1
          elif abcedario.find(i)==-1 and numero.find(i)==-1 and tr.find(i)==-1:
            c+=1
        if (8<=len(str(password))<=16) and a>0 and b>0 and (c>0 or d>0):  
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
           