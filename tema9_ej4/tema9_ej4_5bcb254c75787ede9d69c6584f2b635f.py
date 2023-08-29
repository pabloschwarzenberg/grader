class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        numeros=0
        mayusculas=0
        minisculas=0
        letra=0
        if 8<=len(password)<=16:
          for i in password:
            if i.isspace():
              return False
            elif i.isdigit():
              numeros+=1
            elif i.isupper():
              mayusculas+=1
            elif i.islower():
              minisculas+=1
            elif i.isalpha():
              letra+=1
          if numeros>0 and mayusculas>0 and minisculas>0 and letra>0:
            self.password=clave
          
    def login(self,clave):
        if self.password==clave:
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
           