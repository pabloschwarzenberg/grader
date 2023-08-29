class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre
        self.subcategorias = []

    def incluir(self, taxon):
        self.subcategorias.append(taxon)

# Ejemplo de uso
clase_aves = Taxon("Clase Aves", "Aves")
orden_falconiformes = Taxon("Orden Falconiformes", "Falconiformes")
halcones = Taxon("Familia Falconidae", "Halcones")
