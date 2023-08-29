class Taxon:

    def __init__(self, categoria, nombre):
        self.categoria= categoria
        self.nombre= nombre
        self.clasificacion= []

registro=Taxon("aves","aguila")