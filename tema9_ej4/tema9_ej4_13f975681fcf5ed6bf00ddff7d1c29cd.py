class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""
    def cambiar_password(self,password):
       especiales=["#","_"]
       letras=["a","b","c","d","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
       numeros=["1","2","3","4","5","6","7","8","9"]
       letras2=["A","B","C","D","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
       print(password)
       self.password=password
       i=0
       j=0
       o=0
       p=0
       for caracter in password:
           if caracter in letras2:
              p=p+1
           else:
                p=p
       print(p)
       for caracter in password:
           if caracter in letras:
              j=j+1
           else:
                j=j
       print(j)
       for caracter in password:
           if caracter in numeros:
             i=i+1
           else:
             i=i
       print(i)
       for caracter in password:
           if caracter in especiales:
               o=o+1
           else:
               o=o
       print(o)
       if (8<=len(password)<=16) and (j>0) and (i>0) and ((i<len(password))) and ((o>=1) or p==1): 
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
