class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        mayus=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        num=["1","2","3","4","5","6","7","8","9","0"]
        signos=["#","$","%","&","@","_"]
        c=0
        
        if len(password) >= 8 and len(password)<=16:
          i=0
          while i<len(password):
            if password[i] in mayus:
              c=c+1
              i=i+1
            else:
              i=i+1
          j=0
          while j<len(password):
            if password[j] in num:
              c=c+1
              j=j+1
            else:
              j=j+1
          k=0
          while k<len(password):
            if password[k] in signos:
              c=c+1
              k=k+1
            else:
              k=k+1
          if c>=2:
            self.password=password
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
           