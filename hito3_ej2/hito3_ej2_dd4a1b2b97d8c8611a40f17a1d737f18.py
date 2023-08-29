class Taxon:
    subcategorias=[]    
    def __init__(self,categoria,nombre):
          self.categoria=categoria
          self.nombre=nombre

    def add_subcategoria(self,subcategoria):
         return self.subcategorias.append(subcategoria)
      
    def __str__(self):
          return self.categoria+" "+self.nombre