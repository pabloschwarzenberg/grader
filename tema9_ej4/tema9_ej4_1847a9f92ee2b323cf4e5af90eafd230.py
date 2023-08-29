class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        l=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        n=["1","2","3","4","5","6","7","8","9","0"]
        s=0
        r=0
        if len(password)>=8 and len(password)<=16: 
          for j in range(len(password)):
            letra_clave=password[j]
            if letra_clave in l :
                s=s+1
            elif letra_clave in n:
                r=r+1
          if s+r<len(password):
            self.password=password
            return True
          else :
            return False
        else: 
          return False
            
        
          
        

    def login(self,password):
      if password==self.password:
        return True
      else :
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
           