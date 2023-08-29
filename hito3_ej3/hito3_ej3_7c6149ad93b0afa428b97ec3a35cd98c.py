class Taxon:
    def __init__(self,categoria,nombre):
        self.categoria=categoria
        self.nombre=nombre
        self.subcategorias=list()
    def incluir(self,nombre):
        self.subcategorias.insert(1,nombre)
