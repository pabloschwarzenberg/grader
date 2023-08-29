class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        if 8 <= len(password) <= 16:
          M=0
          N=0
          S=0
          for i in password:
            if i.isupper():
              M=M+1
            if i.isdigit():
              N=N+1  
            if not i.isdigit() and not i.isalpha():
              S=S+1
          if  N>0 and (M>0 or S>0):
            self.password= password
            return True
          else:
            return False
        else:
          return False
           
        
          

    def login(self,password):
       if password == self.password:
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
           