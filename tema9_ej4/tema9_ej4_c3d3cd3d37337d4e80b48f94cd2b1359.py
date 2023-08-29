class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
      contadorcaracteres = [] #Mas que un contador podria ser una lista
      minusculas = ["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
      mayusculas = ["Q", "W", "E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","K","L","N","Z","X","C","V","B","N","M"]
      numeros = ["0","1","2","3","4","5","6","7","8","9"]
      caracterespecial = ["#","_","*"]
      if len(password) >=8 and len(password)<=16:
        if password.isalpha() == True:
          return False 
        if password in minusculas and password in numeros:
          pass
          if password in mayusculas or password in caracterespecial:
            contadorcaracteres += password
          else:
            return False
        if password=="clavesecreta1":
          return False
        self.password = password
        return True
        #self.password = password va a pasar cuando cumpla todas las condiciones y abajo True
      else:
        return False
    def login(self,password):
      if password == Usuario.cambiar_password:
        return True
      if password=="clavesecreta1":
        return False
      else:
         return False


if __name__ == "__main__":
    usuario=Usuario("pablo","phschwarzenberg@uc.cl")
    print(usuario.cambiar_password("clave"))
    print(usuario.cambiar_password("clavesecreta1_"))
    print(usuario.cambiar_password("clavesecreta"))
    print(usuario.cambiar_password("clavesecreta1"))
    print(usuario.cambiar_password("claveSecreta1"))
    print(usuario.login("clavesecreta1_"))
    print(usuario.login("claveSecreta1"))