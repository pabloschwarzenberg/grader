class Taxon:
    def __init__(self, categorizar, nombre):
        self.categoria = categorizar
        self.nombre = nombre
        self.subcategorias = []

    def incluir(taxon_superior, taxon_inferior):
        taxon_superior.subcategorias.append(taxon_inferior)
      