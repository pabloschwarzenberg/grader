class Taxon:
	pass
class Taxon:
    def __init__(self, nombre):
        self.nombre = nombre
        self.subcategorias = []

    def agregar_subcategoria(self, subcategoria):
        self.subcategorias.append(subcategoria)

# Ejemplo de uso
taxon1 = Taxon("Animalia")
taxon2 = Taxon("Chordata")
taxon3 = Taxon("Mammalia")
taxon4 = Taxon("Carnivora")

taxon1.agregar_subcategoria(taxon2)
taxon2.agregar_subcategoria(taxon3)
taxon3.agregar_subcategoria(taxon4)

print(taxon1.nombre)  # Animalia
print(taxon1.subcategorias)  # [Chordata]

print(taxon2.nombre)  # Chordata
print(taxon2.subcategorias)  # [Mammalia]

print(taxon3.nombre)  # Mammalia
print(taxon3.subcategorias)  # [Carnivora]

print(taxon4.nombre)  # Carnivora
print(taxon4.subcategorias)  # []