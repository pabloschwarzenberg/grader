class Taxon:
    def _init_(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre

taxon_aves = Taxon("Clase", "Aves")
print(taxon_aves.categoria) 
print(taxon_aves.nombre)