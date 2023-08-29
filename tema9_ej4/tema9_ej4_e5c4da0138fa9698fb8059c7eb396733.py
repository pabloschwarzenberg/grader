class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        mayus = 0
        especial = 0
        letras = 0
        numeros =0
        if 8<=len(password)<=16:
          for caracter in password:
            if caracter.isalpha() and not caracter.isupper():
              letras+=1
            elif caracter.isalpha() and caracter.isupper():
              mayus+=1
            elif caracter.isdigit():
              numeros+=1
            else:
              especial+=1
          if letras >= 1 and numeros >= 1 and (especial >=1 or mayus >= 1):
            self.password = password
            return True
          else:
            return False
        else:
          return False
           
    def login(self,password):
        if self.password == password:
          return True
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
           