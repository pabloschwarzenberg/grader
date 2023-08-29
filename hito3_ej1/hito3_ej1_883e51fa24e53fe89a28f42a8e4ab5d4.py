class Taxon:
  categoria = ''
  nombre = ''
  
  def __init__(self, categoria, nombre):
    self.categoria = categoria
    self.nombre = nombre
    
  def asignar_categoria(self, categoria):
    self.categoria = categoria
    
  def asignar_nombre(self, nombre):
    self.nombre = nombre
      