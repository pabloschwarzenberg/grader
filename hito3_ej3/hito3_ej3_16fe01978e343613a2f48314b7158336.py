class Taxon:
     def __init__(self,categoria,nombre):
          self.categoria = categoria
          self.subcategorias = []
          self.nombre = nombre
     def incluir(self,subcategorias):
         self.subcategorias.append(Taxon("Falconiformes","Halcon"))
         
	
      