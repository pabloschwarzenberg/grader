class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre
        self.subcategorias = []

taxon1 = Taxon("Mamífero", "Perro")
taxon2 = Taxon("Mamífero", "Gato")

taxon1.subcategorias.append(taxon2)

print(taxon1.subcategorias)

subtaxon = taxon1.subcategorias[0]
print(subtaxon.categoria)
print(subtaxon.nombre)
      