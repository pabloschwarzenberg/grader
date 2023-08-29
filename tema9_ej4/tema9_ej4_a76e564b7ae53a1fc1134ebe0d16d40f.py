class Usuario:
  
  def __init__(self, nombre, email):
    self.nombre = nombre
    self.email = email
    self.clave = ""
  
  def cambiar_password(self, password):
    if 8 <= len(password) <= 16 and (any(c.isupper() for c in password) or any(not c.isalnum() for c in password)):
      self.clave = password
      return True
    else:
      return False
  
  def login(self, password):
    return password == self.clave

# Ejemplo
usuario = Usuario("ValTru", "valt@example.com")
print(usuario.nombre)  # ValTru
print(usuario.email)  # valt@example.com

print(usuario.cambiar_password("password1"))  # False (no cumple las reglas)
print(usuario.cambiar_password("clavesecreta1"))  # True

print(usuario.login("clavesecreta1_"))  # False
print(usuario.login("clavesecreta1"))  # True
