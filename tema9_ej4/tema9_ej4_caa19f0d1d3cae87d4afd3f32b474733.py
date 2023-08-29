class Usuario:
  def __init__(self, nombre, email):
    self.nombre = nombre
    self.email = email 
    self.clave = ""
    
  def cambiar_password(self, password):
    if 8 <= len(password) <= 16 and (any(char.isalpha() for char in password) and any (char.isdigit() for char in password)):
      if any(char.isupper() or not char.isalnum() for char in password):
        self.clave = password
        return True
    return False
    
  def login(self, password):
    return password == self.clave
    
usuario = Usuario("pablo", "phschwarzenberg@uc.cl")
new_password = "MiNewPassword123#"
if usuario.cambiar_password(new_password):
  print("Contrasena cambiada")
else:
  print("La contrasena no cumpe los requisitos")
  
password_ingresada = "IncorrectPassword"
if usuario.login(password_ingresada):
  print("Incio de sesion exitose")
else:
  print("contrasena incorrecta")