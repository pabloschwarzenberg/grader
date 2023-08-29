class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre
        self.subcategorias = []

    def agregar_subcategoria(self, subcategoria):
        self.subcategorias.append(subcategoria)

# Ejemplo de uso
taxon_aves = Taxon("Clase", "Aves")
taxon_orden = Taxon("Orden", "Falconiformes")
taxon_familia = Taxon("Familia", "Accipitridae")

taxon_aves.agregar_subcategoria(taxon_orden)
taxon_orden.agregar_subcategoria(taxon_familia)

print(taxon_aves.subcategorias)  # Output: [<__main__.Taxon object at 0x...>]
print(taxon_orden.subcategorias)  # Output: [<__main__.Taxon object at 0x...>]
