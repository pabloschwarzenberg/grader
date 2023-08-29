def check_password(password):
  special_characters = "!@#$%^&*()-+?_=,<>/"
  if len(password) >= 8 and len(password) <= 16 and any(chr.isdigit() for chr in password):
    if any(chr.isalpha() for chr in password):
      if any(chr.isupper() for chr in password) or any(char in special_characters for char in password):
        return True
  return False
      
class Usuario:
    def __init__(self,nombre,email):
      self.nombre=nombre
      self.email=email
      self.password=""

    def cambiar_password(self,password):
      if check_password(password):
        self.password = password
        return True
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
           