class Taxon:
    def __init__(self, categorias, nombres, taxones=[]):
        self.nombre = nombres
        self.categoria = categorias
        self.subcategorias = taxones
