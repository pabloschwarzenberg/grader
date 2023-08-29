class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.passwurd=""

    def cambiar_password(self,password):
        
        if len(password)>=8 and len(password)<=16:
          abc=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
          num=["0","1","2","3","4","5","6","7","8","9"]
          cabc=0
          cnum=0
          for i in password:
            for j in abc:
              if i==j:
                cabc=cabc+1
            for k in num:
              if k==i:
                cnum=cnum+1
          if (cabc+cnum)<len(password) and cabc>0 and cnum>0:
            self.password=password
            return True
          else:
            return False
        else:
          return False
        pass

    def login(self,password):
        if password==self.password:
          return True
        else: 
          return False
        pass

if __name__ == "__main__":
    usuario=Usuario("pablo","phschwarzenberg@uc.cl")
    print(usuario.cambiar_password("clave"))
    print(usuario.cambiar_password("clavesecreta1_"))
    print(usuario.cambiar_password("clavesecreta"))
    print(usuario.cambiar_password("clasesecreta1"))
    print(usuario.cambiar_password("claveSecreta1"))
    print(usuario.login("clavesecreta1_"))
    print(usuario.login("claveSecreta1"))
           