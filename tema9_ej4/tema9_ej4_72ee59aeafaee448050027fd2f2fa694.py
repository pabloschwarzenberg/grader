class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""
    
    def cambiar_password(self,password):
        mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  
        numeros = 0
        letras = 0
        mayusculas1 = 0
        signos = 0
        for x in password:
          if x in mayusculas:
            mayusculas1 += 1
          elif x.isdigit() == True:
            numeros += 1
          elif x.isalpha() == True:
            letras += 1
          else:
            signos += 1   
        if 8 <= len(password) <= 16 and numeros > 0 and letras > 0:
          if mayusculas1 > 0 or signos > 0:
            self.password += password 
            return True
          else:
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
           