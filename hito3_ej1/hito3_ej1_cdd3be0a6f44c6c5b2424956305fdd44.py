class Taxon:
    def __init__(self,categoria,nombre):
        self.categoria = categoria
        self.nombre = nombre
    def Imprimir(self):
        a = ("{self.categoria},{self.nombre}")
        return a
