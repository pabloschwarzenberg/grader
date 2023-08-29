class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre
        self.subcategorias = []

    def incluir(self, taxon):
        self.subcategorias.append(taxon)

# Crear el taxón "Clase Aves"
aves = Taxon("Clase", "Aves")

# Crear el taxón "Orden Falconiformes"
falconiformes = Taxon("Orden", "Falconiformes")

# Agregar el taxón "Orden Falconiformes" a la lista de subcategorías del taxón "Clase Aves"
aves.incluir(falconiformes)

# Imprimir la lista de subcategorías del taxón "Clase Aves"
print(aves.subcategorias)
