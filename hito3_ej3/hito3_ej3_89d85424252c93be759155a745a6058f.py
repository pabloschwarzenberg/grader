class Taxon:
    def __init__(self, category, name, sub=[]):
        self.nombre = name
        self.categoria = category
        self.subcategorias = sub

    def incluir(self, taxon):
        self.subcategorias.append(taxon)