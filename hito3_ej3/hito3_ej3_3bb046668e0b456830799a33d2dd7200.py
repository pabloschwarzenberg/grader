class Taxon:
    def __init__(self, nombre):
        self.nombre = nombre
        self.subcategorias = []

    def incluir(self, subcategoria):
        self.subcategorias.append(subcategoria)

    def __str__(self):
        return self.nombre