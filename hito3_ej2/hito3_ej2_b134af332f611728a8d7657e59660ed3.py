class Taxon:
    def __init__(self, nombre, categoria, subcategorias):
      self.nombre = nombre
     
      self.subcategorias = []
      
    def registrar(self):
      self.subcategorias.append(self.categoria)