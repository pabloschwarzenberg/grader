class Taxon:
	pass
class Taxon:
    def __init__(self, nombre):
        self.nombre = nombre
        self.subcategorias = []

    def agregar_subcategoria(self, subcategoria):
        self.subcategorias.append(subcategoria)

    def incluir(self, taxon):
        self.subcategorias.append(taxon)

# Ejemplo de uso
taxon1 = Taxon("Animalia")
taxon2 = Taxon("Chordata")
taxon3 = Taxon("Mammalia")
taxon4 = Taxon("Carnivora")
taxon5 = Taxon("Aves")
taxon6 = Taxon("Falconiformes")
taxon7 = Taxon("Halcones")

taxon1.agregar_subcategoria(taxon2)
taxon2.agregar_subcategoria(taxon3)
taxon3.agregar_subcategoria(taxon4)
taxon5.incluir(taxon6)
taxon6.incluir(taxon7)

print(taxon1.nombre)  # Animalia
print(taxon1.subcategorias)  # [Chordata]

print(taxon2.nombre)  # Chordata
print(taxon2.subcategorias)  # [Mammalia]

print(taxon3.nombre)  # Mammalia
print(taxon3.subcategorias)  # [Carnivora]

print(taxon4.nombre)  # Carnivora
print(taxon4.subcategorias)  # []

print(taxon5.nombre)  # Aves
print(taxon5.subcategorias)  # [Falconiformes]

print(taxon6.nombre)  # Falconiformes
print(taxon6.subcategorias)  # [Halcones]

print(taxon7.nombre)  # Halcones
print(taxon7.subcategorias)  # []