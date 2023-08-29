class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre

class Aves(Taxon):
    def __init__(self, nombre):
        super().__init__("Clase Aves", nombre)

      