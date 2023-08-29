class Taxon:
    def __init__(self,cat,name):
        self = self
        self.categoria = cat
        self.nombre = name
        self.subcategorias = []

    def incluir(self,otro):
        a = self.subcategorias
        a.append(otro)