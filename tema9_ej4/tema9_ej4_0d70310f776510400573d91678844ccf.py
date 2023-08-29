class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
      if len(password)=>8 and len(password)<=16:
        if password.isalnum()==True: #isalnum->revisa si string tiene numeros y letras y retorna true si es asi
          if(password.islower()==False) or #caracter especial password:
            return True
      else:
        return False
        
      

    def login(self,password):
        if cambiar_password(self,password)==self.password:
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
           