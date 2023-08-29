class Taxon:
    def __init__(self,c,n):
        self.categoria = c
        self.nombre = n
        self.subcategorias = []
    def incluir(self,t):
        self.subcategorias.append(t) 
