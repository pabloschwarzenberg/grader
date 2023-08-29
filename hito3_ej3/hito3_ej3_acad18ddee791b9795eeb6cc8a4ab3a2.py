class Taxon:
  def __init__ (self,categoria,nombre, subcategorias=[]):
   self.categoria=categoria
   self.nombre=nombre
   self.subcategorias=subcategorias
  def __str__ (self):
   return self.categoria + " " + self.nombre
  def incluir(self, nuevo):
   self.subcategorias.append(nuevo)