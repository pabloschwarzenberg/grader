class Taxon:
  def __init__(self, c, n, subcategorias = None):
    self.categoria = c
    self.nombre = n
    if subcategorias is None:
      subcategorias = []
    self.subcategorias = subcategorias
  def incluir(self, taxon):
    self.subcategorias.append(taxon)
    
aves = Taxon("animales", "aves")
falconiformes = Taxon("aves", "falconiformes")
halcones = Taxon("falconiformes", "halcones")

aves.incluir(falconiformes)
falconiformes.incluir(halcones)

print(aves.subcategorias)
print(falconiformes.subcategorias)

      