# Importar el módulo re para usar expresiones regulares
import re

# Definir la clase Usuario
class Usuario:
  # Inicializar los atributos de la clase
  def __init__(self, nombre, email):
    self.nombre = nombre
    self.email = email
    self.clave = "" # Inicializar la clave como un string vacío

  # Definir un método para cambiar la clave del usuario
  def cambiar_clave(self, clave):
    # Validar que la clave tenga entre 8 y 16 caracteres
    if len(clave) < 8 or len(clave) > 16:
      return False # Retornar False si no cumple la condición
    # Validar que la clave contenga letras y números
    if not re.search("[a-zA-Z0-9]", clave):
      return False # Retornar False si no cumple la condición
    # Validar que la clave contenga al menos una letra mayúscula o un carácter especial
    if not re.search("[A-Z]|[^\w]", clave):
      return False # Retornar False si no cumple la condición
    # Si la clave cumple todas las condiciones, actualizar el atributo clave y retornar True
    self.clave = clave
    return True

  # Definir un método para iniciar sesión con una clave
  def login(self, clave):
    # Comparar la clave ingresada con la clave del usuario
    if clave == self.clave:
      return True # Retornar True si son iguales
    else:
      return False # Retornar False si son diferentes

# Crear un objeto de la clase Usuario con el nombre y el email que quieras
observado = Usuario("Juan", "juan@gmail.com")

# Usar el método cambiar_clave para asignarle una clave al objeto observado
o=observado.cambiar_clave("clave")
           