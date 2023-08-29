class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre
        self.subcategorias = []

    def incluir(self, taxon):
        self.subcategorias.append(taxon)


taxon1 = Taxon("", "")
taxon2 = Taxon("", "")

taxon1.incluir(taxon2)

print(taxon1.subcategorias)  

      