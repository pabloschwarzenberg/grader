class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        abecedario_1=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        abecedario_2=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
        especial=["!","#","&","$","%","_","-"]
        numeros =["0","1","2","3","4","5","6","7","8","9"]
        if (8 <= len(password)) and  (len(password)<= 16):
          i=0
          j=0
          k=0
          for letra in password:
              if (letra in abecedario_1) or (letra in especial):
                  i=i+1
              if letra in abecedario_2:
                  j=j+1
              if letra in numeros:
                  k=k+1
           
          if (i!=0) and (j!=0) and (k!=0):
              self.password=password
              return True
          elif (i ==0):
              return False

          elif (j == 0):
              return False

          elif (k==0):
              return False
         
        else:
            return False
    def login(self,password):
        if self.password == password:
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