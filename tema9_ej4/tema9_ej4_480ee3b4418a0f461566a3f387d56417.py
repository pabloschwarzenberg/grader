import string
class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
      valido=True
      if len(password)<8 or len(password)>16:
        valido=False
      minusculas=list(string.ascii_lowercase)
      mayusculas=list(string.ascii_uppercase)
      numeros=[0,1,2,3,4,6,7,8,9]
      tiene_numero=False
      tiene_letra=False
      tiene_simbolo_mayusculas=False
      for i in password:
        if i in minusculas:
          tiene_letra=True
        if i in mayusculas:
          tiene_simbolo_mayuscula=True
          tiene_letra=True
        if i in numeros:
          tiene_numero=True
        if i not in minusculas and i not in mayusculas and i not in numeros:
          tiene_simbolo_mayuscula=True
      if tiene_letra==False or tiene_numero==False or tiene_simbolo_mayuscula==False:
        valido=False
      if valido==True:
        self.password=password 
        return True
      elif valido==False:
        return False
        
        pass

    def login(self,password):
        if password== self.password:
          return True
        elif password !=self.password:
          return False
          
        
        pass

if __name__ == "__main__":
    usuario=Usuario("pablo","phschwarzenberg@uc.cl")
    print(usuario.cambiar_password("clave"))
    print(usuario.cambiar_password("clavesecreta1_"))
    print(usuario.cambiar_password("clavesecreta"))
    print(usuario.cambiar_password("clasesecreta1"))
    print(usuario.cambiar_password("claveSecreta1"))
    print(usuario.login("clavesecreta1_"))
    print(usuario.login("claveSecreta1"))
           