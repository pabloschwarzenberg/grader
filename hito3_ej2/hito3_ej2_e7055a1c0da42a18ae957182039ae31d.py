class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre
        self.subcategorias = []

# Ejemplo de uso
taxon_clase_aves = Taxon("Clase", "Aves")
taxon_orden_falconiformes = Taxon("Orden", "Falconiformes")
taxon_familia_falconidae = Taxon("Familia", "Falconidae")

# Establecer las relaciones jerárquicas
taxon_clase_aves.subcategorias.append(taxon_orden_falconiformes)
taxon_orden_falconiformes.subcategorias.append(taxon_familia_falconidae)
