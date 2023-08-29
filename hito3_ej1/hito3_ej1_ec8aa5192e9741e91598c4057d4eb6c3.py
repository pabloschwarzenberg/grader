class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre


ave = Taxon("Clase", "Aves")
print(ave.categoria)  # Output: Clase
print(ave.nombre)  # Output: Aves