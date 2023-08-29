class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre
        self.subcategorias = []

    def agregar_subcategoria(self, subcategoria):
        self.subcategorias.append(subcategoria)

    def incluir(self, taxon):
        self.subcategorias.append(taxon)

# Ejemplo de uso
aves = Taxon("Clase", "Aves")
aves.agregar_subcategoria(Taxon("Orden", "Passeriformes"))
aves.agregar_subcategoria(Taxon("Orden", "Psittaciformes"))

falconiformes = Taxon("Orden", "Falconiformes")
aves.incluir(falconiformes)

print(aves.subcategorias)
