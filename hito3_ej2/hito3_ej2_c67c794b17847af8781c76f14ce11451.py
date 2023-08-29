class Taxon:
    categoria = ""
    nombre = ""
    def __init__(self,categoria,nombre):
        self.categoria = categoria
        self.nombre = nombre
    pass
class jerarquia(Taxon):
    def __init__(self,categoria,nombre,subcategorias=None):
    super().__init__(self,categoria,nombre)
    self.subcategoria = []
    pass