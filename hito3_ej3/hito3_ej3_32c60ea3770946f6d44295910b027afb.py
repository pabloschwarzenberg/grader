class Taxon:
	pass
class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre
        self.subcategorias = []

    def incluir(self, taxon):
        self.subcategorias.append(taxon)

# Ejemplo de uso
aves = Taxon("Clase", "Aves")
falconiformes = Taxon("Orden", "Falconiformes")
halcones = Taxon("Familia", "Halcones")

aves.incluir(falconiformes)
falconiformes.incluir(halcones)

print(aves.subcategorias)  # Salida: [<__main__.Taxon object at 0x7f0a55f89f40>]
print(falconiformes.subcategorias)  # Salida: [<__main__.Taxon object at 0x7f0a55f89fd0>]
