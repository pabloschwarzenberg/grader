class Taxon:
    def __init__ (self,categoria,nombre):
      self.categoria = categoria
      self.nombre = nombre
      self.subcategorias = []
    def set_subcategorias(self,subcategoria):
      self.subcategorias.append(subcategoria)
    def incluir(self,other):
      self.set_subcategorias(other)

other = Taxon("Falconiformes","Halcones")
self1 = Taxon("Aves", "Aves")
self1.incluir(other)
