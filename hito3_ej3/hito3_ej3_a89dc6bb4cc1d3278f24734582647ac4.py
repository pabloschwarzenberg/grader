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
halcon = Taxon("Familia", "Halcon")
halcon.incluir(Taxon("Género", "Falco"))
falconiformes.incluir(halcon)
aves.incluir(falconiformes)

# Acceso a las subcategorías
print(aves.subcategorias)                   # Imprime una lista con falconiformes
print(aves.subcategorias[0].subcategorias)  # Imprime una lista con halcon
print(aves.subcategorias[0].subcategorias[0].subcategorias)  # Imprime una lista vacía []

