class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
      abc=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
      ABC=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
      num=["0","1","2","3","4","5","6","7","8","9"]
      pas=str(password)
      i=0
      if len(pas)<8 or len(pas)>16:
        return False
      m=0
      M=0
      nume=0
      r=0
      while i<len(pas):
        if pas[i] in abc:
          m=1+m
        if pas[i] in ABC:
          M=1+M
        if pas[i] in num:
          nume=1+nume
        i=i+1
      if len(pas)!=(M+m+nume):
        r=1
      if m>0 and M>0 and nume>0:
        self.password=password
        return True
      if m>0 and r>0 and nume>0:
        self.password=password
        return True
      return False


    def login(self,password):
      if password==self.password:
        return True
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
           