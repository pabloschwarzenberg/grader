class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre
        self.subcategorias = []
        
clase_aves = Taxon("Clase", "Aves")

orden_passeriformes = Taxon("Orden", "Passeriformes")
orden_falconiformes = Taxon("Orden", "Falconiformes")

clase_aves.subcategorias.append(orden_passeriformes)
clase_aves.subcategorias.append(orden_falconiformes)
