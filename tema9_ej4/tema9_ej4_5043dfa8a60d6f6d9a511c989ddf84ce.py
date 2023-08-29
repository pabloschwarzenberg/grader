class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        p=False
        if len(password)>=8 and len(password)<=16:
          L=list(password)
          numeros=["0","1","2","3","4","5","6","7","8","9"]
          letras=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
          Letras=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
          simb=["+","-","#","?","¿","¡","!","*","_"]
          l=0
          n=0
          M=0
          s=0
          for i in range(len(L)):
            for j in range(len(letras)):
              if L[i]==letras[j]:
                print(L[i],letras[j])
                l=1
          for i in range(len(L)):
            for j in range(len(Letras)):
              if L[i]==Letras[j]:
                M=1
                print(L[i],Letras[j])
          for i in range(len(L)):
            for j in range(len(simb)):
              if L[i]==simb[j]:
                s=1
                print(L[i],simb[j])
          for i in range(len(L)):
            for j in range(len(numeros)):
              if L[i]==numeros[j]:
                print(L[i],numeros[j])
                n=1
          if l==1 and n==1:
            if (M==1):
              self.password=password
              p=True
            if s==1:
              self.password=password
              p=True
        return p

    def login(self,password):
        print(password)
        if self.password==password:
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
           
