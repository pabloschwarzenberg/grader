class Taxon:
    def __init__(self, nombre, categoria):
        self.categoria = 'Clase'
        self.nombre = 'Aves'
        self.subcategorias = []

    def incluir(self, taxon):
        self.subcategorias.append(taxon)
