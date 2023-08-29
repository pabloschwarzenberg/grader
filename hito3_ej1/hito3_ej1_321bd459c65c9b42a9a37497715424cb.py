class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre

# Ejemplo de uso
taxon_aves = Taxon("Clase", "Aves")
print("Categoría:", taxon_aves.categoria)
print("Nombre:", taxon_aves.nombre)

      