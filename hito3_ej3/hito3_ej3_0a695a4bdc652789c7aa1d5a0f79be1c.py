class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre
        self.subcategorias = []

    def incluir(self, subcategoria):
        self.subcategorias.append(subcategoria)

# Ejemplo de uso
taxon_aves = Taxon("Clase", "Aves")
taxon_falconiformes = Taxon("Orden", "Falconiformes")
taxon_halcones = Taxon("Familia", "Halcones")

taxon_aves.incluir(taxon_falconiformes)
taxon_falconiformes.incluir(taxon_halcones)

print(taxon_aves.subcategorias)  # Output: [<__main__.Taxon object at 0x...>]
print(taxon_falconiformes.subcategorias)  # Output: [<__main__.Taxon object at 0x...>]
