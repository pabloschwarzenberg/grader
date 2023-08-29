class Usuario:
  def __init__(self,nombre,email):
    self.nombre=nombre
    self.email=email
    self.password=""

  def cambiar_password(self,password):
    if 8<= len(password) <=16:
      num = False
      let = False
      especial = False
      mayus = False
      for caracter in password:
        if caracter.isdigit() == True:
          num = True
        if caracter.isalpha() == True:
          let = True
        if caracter.isalnum() == False:
          especial = True
        if caracter.isupper() == True:
          mayus = True
      if num and let and (especial or mayus):
         self.password = password
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
           