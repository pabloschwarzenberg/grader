class Taxon:
    def __init__(self,categoria,nombre):
        self.categoria=categoria
        self.nombre=nombre
    def imprimir(self):
        print("el ave avistada es", self.categoria, self.nombre)
    pass        