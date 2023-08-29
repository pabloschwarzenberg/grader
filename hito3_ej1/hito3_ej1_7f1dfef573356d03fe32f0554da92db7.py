class Taxon:
    def __init__(self,categoria,nombre):
        self.categoria = categoria
        self.nombre = nombre
    def darCategoria(self):
        return self.categoria
    def darNombre(self):
        return self.nombre