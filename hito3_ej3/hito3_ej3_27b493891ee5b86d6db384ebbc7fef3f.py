class Taxon:
    def __init__(self, c, n, s=None):
        if s is None:
         s = []
        self.categoria = c
        self.nombre = n
        self.subcategorias = s

    def incluir(self, n):
         self.subcategorias.append(n)