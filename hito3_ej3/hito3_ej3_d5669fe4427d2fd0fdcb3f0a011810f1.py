class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre
        self.subcategorias = []

    def incluir(self, taxon):
        if isinstance(taxon, Taxon):
            self.subcategorias.append(taxon)
        else:
            raise ValueError("El parámetro 'taxon' debe ser una instancia de la clase Taxon")
