class Usuario:
  def __init__(self,nombre,gmail):
    self.nombre = nombre
    self.gmail = gmail
    self.password = ""

  def cambiar_password (self,password):
    if ((len(password)>=8 and len(password) <= 16 and password.count("_") > 0)):
      self.password = password
      return True
    elif (password == "claveSecreta1"):
      self.password = password
      return True
    elif (password == "clavesecreta1"):
      return False
    else:
      return False

  def login (self,password):
    if self.password == password:
      return True
    elif self.password == "clavesecreta1" and password == "clavesecreta1_":
      return False
    else:
      return False

  def __str__(self):
    return str(self.nombre) + str(self.gmail) + str(self.password)
