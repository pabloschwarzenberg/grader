#ORNITOLOGIA 2
class Taxon:
 def __init__(self, categoria, nombre):
  self.nombre = nombre
  self.categoria = categoria

class Taxon:
 def __init__(self, categoria, nombre):
  self.nombre = nombre
  self.categoria = categoria
  self.subcategorias = []

class Taxon:
 def __init__(self, categoria, nombre):
  self.nombre = nombre
  self.categoria = categoria
  self.subcategorias = []
 def incluir(self, taxon):
  self.subcategorias.append(taxon)

