subcategorias=[]
class Taxon:
    def __init__(self,categoria,nombre,subcategorias):
        self.nombre = nombre
        self.categoria = categoria
        self.subcategorias = subcategorias
        pass
class subcategoria(Taxon):
    grupo=[]