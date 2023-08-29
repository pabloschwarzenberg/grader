class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        x=password
        abc="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
        num="0123456789"
        c=0
        d=0
        if 8<=len(password)<=16:
          for i in list(num):
            if password.count(i)>0:
              d=d+1
            x=x.replace(i,"")
          for i in list(abc):
            if password.count(i)>0:
              c=c+1
          for i in list(abc.lower()): 
            x=x.replace(i,"")
          if d>0 and (c>0 or len(x)>0):
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
           