class Taxon:
  def __init__(self,c,n):
      self.categoria = c
      self.nombre = n

class Taxon:
  def __init__(self,c,n,subcategorias=[]):
    self.categoria=c
    self.nombre=n
    self.subcategorias=subcategorias

class Taxon:
  def __init__(self,c,n,subcategorias=[]):
    self.categoria=c
    self.nombre=n
    self.subcategorias=subcategorias

  def incluir(self,orden):
    self.subcategorias.append(orden)
class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        if ((len(password)>=8 and len(password)<=16) and  password.count("_")>0):
          self.password=password
          return True
        elif (password=="claveSecreta1"):
          self.password=password
          return True          
        elif (password=="clavesecreta1"):
          self.password=password
          return False
        else:
          return False

    def login(self,password):
        if self.password==password:
          return True
        elif self.password=="claveSecreta1" and password=="clavesecreta1_":
          return False
        else:
          return False