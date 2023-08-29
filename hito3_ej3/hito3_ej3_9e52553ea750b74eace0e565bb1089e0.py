class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre
        self.subcategorias = []

    def incluir(self, taxon):
        self.subcategorias.append(taxon)

# Ejemplo de uso
clase_aves = Taxon("Clase", "Aves")
orden_falconiformes = Taxon("Orden", "Falconiformes")
halcones = Taxon("Familia", "Halcones")

clase_aves.incluir(orden_falconiformes)
orden_falconiformes.incluir(halcones)

print(clase_aves.subcategorias)  # Salida: [<__main__.Taxon object at 0x...>]
print(orden_falconiformes.subcategorias)  # Salida: [<__main__.Taxon object at 0x...>]
