class Taxon:
    def __init__(self,categoria,nombre,subcategorias = []):
        self.categoria = categoria
        self.nombre = nombre
        self.subcategorias = subcategorias
    def darCategoria(self):
        return self.categoria
    def darNombre(self):
        return self.nombre
    def darSubcategorias(self):
        return self.categorias