class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.clave = ""
        self.password = ""
    def __str__(self):
        return self.clave
        
    def cambiar_password(self,password):
      self.password = password
      clave = self.clave

      if len(password) >= 8 and len(password) <= 16:
          for i in range(0,10):
              if password.find("1") != -1:
                  if password.find("S") != -1 or password.find("_") != -1:
                      self.clave = password
                      return(True)
                      
                      
                  else: 
                      return(False) 
              else: 
                  return(False)  
      else: 
          return(False) 
        
    def login(self,password):
      if self.clave == password:
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
           
           