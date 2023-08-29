class Taxon:
    def __init__(self,categoria,nombre):
        self.categoria = categoria
        self.nombre = nombre
        self.subcategorias = []
c1 = Taxon("Clase","Aves")
c1.nombre = "Clase"
c1.categoria = "Aves"
c1.subcategorias = []