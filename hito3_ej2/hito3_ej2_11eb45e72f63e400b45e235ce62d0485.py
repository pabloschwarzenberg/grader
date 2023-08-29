class Taxon:
 def __init__ (self,categoria,nombre):
   self.categoria=categoria
   self.nombre=nombre
 def __str__(self):
   return "categoria: {}\n nombre:{}\n".format(self.categoria,self.nombre)
class categorias(Taxon):
 lista= list()
