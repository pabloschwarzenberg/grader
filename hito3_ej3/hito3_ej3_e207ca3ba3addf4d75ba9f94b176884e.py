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

print(ave.subcategorias)  # Salida: [<__main__.Taxon object at 0x...>]
print(ave.subcategorias[0].categoria)  # Salida: Orden
print(ave.subcategorias[0].nombre)  # Salida: Falconiformes
