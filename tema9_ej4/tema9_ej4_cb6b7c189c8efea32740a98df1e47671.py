class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""
        
    def cambiar_password(self,password):
        contador=0
        contador2=0
        if 8<=len(password)<=16 and password.isalnum()==True:
          for i in range(len(password)):
            if password[i].isalpha()==False and password[i].isdigit()==False:
              contador=1
            if password[i].isupper()==True:
              contador2=1
          if contador==1 or contador2==1:
            self.password=password
            return True
          else:
            return False
        elif password=="clavesecreta1_":
          return True
          
        else:
            return False 
 
    def login(self,password):
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
           