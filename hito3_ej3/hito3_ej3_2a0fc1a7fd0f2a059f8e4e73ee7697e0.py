class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre
        self.subcategorias = []

    def incluir(self, taxon):
        self.subcategorias.append(taxon)
        
clase_aves = Taxon("Clase", "Aves")
orden_falconiformes = Taxon("Orden", "Falconiformes")
familia_accipitridae = Taxon("Familia", "Accipitridae")

clase_aves.incluir(orden_falconiformes)
orden_falconiformes.incluir(familia_accipitridae)