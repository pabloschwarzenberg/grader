class Taxon:
    def __init__(self, nombre, subcategorias=None):
        self.nombre = nombre
        self.subcategorias = [] if subcategorias is None else subcategorias
