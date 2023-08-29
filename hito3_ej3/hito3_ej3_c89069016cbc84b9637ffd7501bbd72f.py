class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre
        self.subcategorias = []

    def incluir(self, taxon):
        self.subcategorias.append(taxon)

# Ejemplo de uso
taxon_clase_aves = Taxon("Clase", "Aves")
taxon_orden_falconiformes = Taxon("Orden", "Falconiformes")
taxon_halcones = Taxon("Familia", "Halcones")

taxon_clase_aves.incluir(taxon_orden_falconiformes)
taxon_orden_falconiformes.incluir(taxon_halcones)

print(taxon_clase_aves.subcategorias)  # Output: [<__main__.Taxon object at 0x...>]
print(taxon_orden_falconiformes.subcategorias)  # Output: [<__main__.Taxon object at 0x...>]
