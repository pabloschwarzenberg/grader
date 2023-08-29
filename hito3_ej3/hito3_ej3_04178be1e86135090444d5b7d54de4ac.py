class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre
        self.subcategorias = []
    def incluir(self, nuevo_taxon):
        self.subcategorias.append(nuevo_taxon)