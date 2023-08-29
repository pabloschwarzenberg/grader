class Taxon:
  def __init__(self,ca,n):
    self.categoria= ca
    self.nombre= n
  def __str__(self):
    return "ave:\nCategoria: "+self.categoria+"\nNombre: "+self.nombre
#principal
print("\tClase de Aves:")
ave1= Taxon("Clase", "Aves")
print("\n",ave1)