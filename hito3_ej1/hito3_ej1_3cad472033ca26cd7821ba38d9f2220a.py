class Taxon:
    def __init__(self, categoria, nombre, subcat=[]):
        self.nombre = nombre
        self.categoria = categoria
        self.subcategorias = subcat
    pass