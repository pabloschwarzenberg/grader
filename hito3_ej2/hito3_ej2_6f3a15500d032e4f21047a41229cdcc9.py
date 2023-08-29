class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre
        self.subcategorias = []

# Ejemplo de uso
aves = Taxon("Clase", "Aves")
falconiformes = Taxon("Orden", "Falconiformes")
aves.subcategorias.append(falconiformes)

print(aves.subcategorias[0].nombre)  # Imprime "Falconiformes"

     