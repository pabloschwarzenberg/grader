class Taxon:

    def __init__(self,categoria,nombre):
        self.subcategorias = []
        self.categoria = categoria
        self.nombre = nombre

    def __str__(self):

        return str(self.categoria)+" "+str(self.nombre)

    def incluir(self,taxon):
        
        self.subcategorias.append(taxon)