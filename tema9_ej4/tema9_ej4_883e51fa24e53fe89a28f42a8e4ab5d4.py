class Usuario():
  """
  Representa a un usuario de un sitio web o red social
  """
  def __init__(self, nombre, email):
    """
    Inicializa la clase Usuario con su nombre y email
    """
    self.nombre = nombre
    self.email = email
    self.password = ""

  def cambiar_password(self, password):
    """
    Cambia la password del usuario
    """
    if len(password) >= 8 and len(password) <= 16:
      tiene_letras = False
      tiene_numeros = False
      tiene_simbolos = False
      tiene_mayusculas = False
      for caracter in password:
        if caracter.isalpha():
          tiene_letras = True
        elif caracter.isdigit():
          tiene_numeros = True
        elif caracter.islower():
          tiene_mayusculas = False
           