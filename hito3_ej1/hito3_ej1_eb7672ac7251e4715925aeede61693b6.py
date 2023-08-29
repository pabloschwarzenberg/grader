class Taxon:
    def __init__(self,categoria,nombre):
        self.categoria=categoria
        self.nombre=nombre
    def __repr__(self):
        s=""
        s=s+self.categoria
        s=s+":" + str(self.nombre)
        return s
    pass