class Taxon:
    def init(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre


ave = Taxon("Clase", "Aves")
print(ave.categoria)
print(ave.nombre)