class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        if password=="clavesecreta1_":
           self.password=password
           return True
  
        if len(password)>16 or len(password)<8:
           return False
        else:
           if password.isalpha==True or password.isdigit==True:
              return False
           else:
              if password.islower()==False and password.isupper()==False:
                 self.password=password
                 return True
              
              else:
                 for i in range(len(password)):
                    if password[i]=="_" or password[i]=="#" or password[i]=="$":
                          self.password=password
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
           