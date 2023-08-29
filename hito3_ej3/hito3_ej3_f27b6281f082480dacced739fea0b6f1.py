class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre
        self.subcategorias = []

    def incluir(self, taxon):
        self.subcategorias.append(taxon)

# Ejemplo de uso
ave = Taxon("Clase", "Aves")
falconiformes = Taxon("Orden", "Falconiformes")
ave.incluir(falconiformes)

print(ave.categoria)  # Salida: Clase
print(ave.nombre)  # Salida: Aves
print(len(ave.subcategorias))  # Salida: 1
print(ave.subcategorias[0].nombre)  # Salida: Falconiformes
