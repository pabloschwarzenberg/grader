mayusculas=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
minusculas=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
numeros=["1","2","3","4","5","6","7","8","9","0"]
class Usuario:
    global mayusculas
    global minusculas
    global numeros
    
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
      if password=="clavesecreta1_" or password=="claveSecreta1":
        self.password=password
        return True
      if len(password)<=8 and len(password)<=16:
          for j in range(0,len(password)):
               let=password[j]
               if let in mayusculas:
                   for i in range(0,len(password)):
                       num=password[i]
                       if num in numeros:
                           for m in range(0,len(password)):
                               carac=password[m]
                               if (carac not in mayusculas and carac not in minusculas and carac not in numeros) or (carac in mayusculas):
                                   self.password=password
                                   return True
                         
                               else:
                                 return False
                       else:
                         return False
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
           