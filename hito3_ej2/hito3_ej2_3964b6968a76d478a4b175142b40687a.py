class Taxon:
    def __init__(self, nuevacategoria, nuevonombre):
        self.categoria = nuevacategoria
        self.nombre = nuevonombre
        self.subcategorias = []
        