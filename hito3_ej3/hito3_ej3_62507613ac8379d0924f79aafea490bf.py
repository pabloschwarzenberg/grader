class Taxon:
    def __init__(self,a,b,subcategorias=[]):
        self.categoria=a
        self.nombre=b
        self.subcategorias=subcategorias

    def incluir(self,Informe):
        self.subcategorias.append(Informe)