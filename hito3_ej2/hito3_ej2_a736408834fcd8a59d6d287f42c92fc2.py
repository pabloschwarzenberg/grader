class Taxon:
    def __init__(self,nombre,categoria):
        self.nombre = self.__class__.__name__
        self.categoria = None
        self.subcategorias = []

    def agregar_subcategoria(self, subcategoria):
        self.subcategorias.append(subcategoria)