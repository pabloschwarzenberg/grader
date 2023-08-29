class Taxon:
    def __init__(self, nombre, categoria):
      self.nombre = nombre
      self.categoria = categoria
      self.subcategorias = []
      
    def incluir(self,categoria):
      self.subcategorias.append(self.categoria)
      