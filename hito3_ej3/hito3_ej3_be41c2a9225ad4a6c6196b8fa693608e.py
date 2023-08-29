class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre
        self.subcategorias = []

    def incluir(self, taxon):
        self.subcategorias.append(taxon)

aves = Taxon("Clase", "Aves")
falconiformes = Taxon("Orden", "Falconiformes")
halcones = Taxon("Familia", "Halcones")

falconiformes.incluir(halcones)
aves.incluir(falconiformes)

print(aves.categoria)                 
print(aves.nombre)                   
print(len(aves.subcategorias))       
print(aves.subcategorias[0].nombre)
print(len(aves.subcategorias[0].subcategorias))   
print(aves.subcategorias[0].subcategorias[0].nombre)   

      