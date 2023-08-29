class Usuario:
  def __init__(self, nombre, email):
    self.nombre = nombre
    self.email = email
    self.clave = ""
  def cambiar_password(self, password):
    #Validar
    if len(password) < 8 or len(password) > 16:
      return False
    has_letter = False
    has_number = False
    has_special = False
    for char in password:
      if char.isalpha():
        has_letter = True
      elif char.isdigit():
        has_number = True
      else:
        has_special = True
    if(has_letter and has_number) or has_special:
      self.clave = password
    return False
  def login(self, password):
    return self.clave == password
#Programa
#Crear usuario
usuario = Usuario("John Doe", "johndoe@example.com")
if usuario.cambiar_password("MiClave123#"):
  print("Contraseña cambiada exitosamente")
else:
  print("La contrasena no cumple con las reglas")
#Iniciar sesion
if usuario.login("MiClave123#"):
  print("Inicio de sesion exitoso")
else:
  print("Contraseña incorrecta")