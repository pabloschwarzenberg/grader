class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre
        self.subcategorias = []

    def incluir(self, taxon):
        self.subcategorias.append(taxon)

# Ejemplo de uso
aves = Taxon("Clase", "Aves")
orden = Taxon("Orden", "Falconiformes")
familia = Taxon("Familia", "Falconidae")

aves.incluir(orden)
orden.incluir(familia)

print(aves.subcategorias)  # Output: [<__main__.Taxon object at 0x...>]
print(orden.subcategorias)  # Output: [<__main__.Taxon object at 0x...>]
print(familia.subcategorias)  # Output: []
