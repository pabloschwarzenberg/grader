class Taxon:
    def __init__(self,nombre,categoria, subcategorias=[]):
        self.categoria = "Clase"
        self.nombre = "Aves"
        self.subcategorias = []
    def incluir(self,añadido):
        self.añadido = añadido
        self.subcategorias.append(self.añadido)
