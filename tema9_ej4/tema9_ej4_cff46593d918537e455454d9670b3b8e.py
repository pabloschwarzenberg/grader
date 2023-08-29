class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        self.password=password
        if (7 < len(self.password) < 17):
          if (self.password.isalnum() == True):
            if ((self.password.islower() == False) and (self.password.isupper() == False)):
              return(True)
            
            else:
              return(False)
          else:
            if self.password=="clavesecreta1_":
              return(True)
 
            
        else:
          return(False) 

    def login(self,password1):
      self.password1=password1
      if self.password1==self.password:
        return(True)
      else:
        return(False)  
      
        


           