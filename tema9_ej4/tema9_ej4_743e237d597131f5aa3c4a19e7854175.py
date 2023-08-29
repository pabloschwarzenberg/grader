class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        digito = False
        mayusCaracter = False
        
        if len(password) > 7 and len(password) < 17:
            for i in password:
              if i.isdigit():
                digito = True
              elif i.isupper():
                mayusCaracter = True
              elif i.isalpha() == False and i.isdigit() == False:
                mayusCaracter = True
        if digito == True and mayusCaracter == True:
             self.password = password
             return True
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
           