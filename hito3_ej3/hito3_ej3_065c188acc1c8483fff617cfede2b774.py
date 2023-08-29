class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre
        self.subcategorias = []

    def incluir(self, taxon):
        self.subcategorias.append(taxon)

# Ejemplo de uso de la clase Taxon
introducir = Taxon("Aves", "Aves")
print(introducir.categoria)  # Imprime "Aves"
print(introducir.nombre)  # Imprime "Aves"
print(introducir.subcategorias)  # Imprime []

halcones = Taxon("Orden", "Falconiformes")
introducir.incluir(halcones)

print(introducir.subcategorias)  # Imprime [<__main__.Taxon object at 0x00000123456789>]
