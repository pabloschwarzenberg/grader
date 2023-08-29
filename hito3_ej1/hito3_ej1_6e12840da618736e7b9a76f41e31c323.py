class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre
aves = Taxon("Clase", "Aves")
print(aves.categoria)  # Salida: Clase
print(aves.nombre)     # Salida: Aves
