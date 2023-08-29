class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre

# Ejemplo de uso
taxon_aves = Taxon("Clase", "Aves")
print(taxon_aves.categoria)  # Output: Clase
print(taxon_aves.nombre)  # Output: Aves
