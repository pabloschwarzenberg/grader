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

# Imprimir la lista de subcategorias
for subcategoria in taxon_clase_aves.subcategorias:
    print(subcategoria.nombre)
