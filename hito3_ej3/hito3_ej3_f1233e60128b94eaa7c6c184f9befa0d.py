class Taxon:
    def __init__(self, nombre):
        self.nombre = nombre
        self.subcategorias = []

    def agregar_subcategoria(self, subcategoria):
        self.subcategorias.append(subcategoria)

    def incluir(self, taxon):
        self.subcategorias.append(taxon)

    def obtener_subcategorias(self):
        return self.subcategorias


# Ejemplo de uso
animalia = Taxon("Animalia")
chordata = Taxon("Chordata")
aves = Taxon("Aves")
falconiformes = Taxon("Falconiformes")
halcones = Taxon("Halcones")

animalia.agregar_subcategoria(chordata)
chordata.agregar_subcategoria(aves)
aves.incluir(falconiformes)
falconiformes.incluir(halcones)

print(animalia.obtener_subcategorias())  # Output: [<__main__.Taxon object at 0x00000123456789>]
print(chordata.obtener_subcategorias())  # Output: [<__main__.Taxon object at 0x00000123456789>]
print(aves.obtener_subcategorias())  # Output: [<__main__.Taxon object at 0x00000123456789>]
print(falconiformes.obtener_subcategorias())  # Output: [<__main__.Taxon object at 0x00000123456789>]
print(halcones.obtener_subcategorias())  # Output: []

     