class Taxon:
    def __init__ (self,categoria,nombre):
      self.categoria = categoria
      self.nombre = nombre
      self.subcategorias = []
    def set_subcategoria(self, subcategoria):
      self.subcategoria.append(subcategoria)
      