 class Taxon:
   def __init__(self,c,n):
       self.categoria = c
       self.nombre = n
       self.subcategorias = []
   def incluir(self,Taxon):
      self.subcategorias.append(Taxon)
       
clase_aves = Taxon("Clase", "Aves")
orden_falconiformes = Taxon("Orden", "Falconiformes")
halcones = Taxon("Género", "Halcones")

clase_aves.incluir(orden_falconiformes)
orden_falconiformes.incluir(halcones)
