class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre
        self.subcategorias = []

# Ejemplo de uso
aves = Taxon("Clase", "Aves")
orden = Taxon("Orden", "Falconiformes")
familia = Taxon("Familia", "Falconidae")

aves.subcategorias.append(orden)
orden.subcategorias.append(familia)

print(aves.subcategorias)  # Output: [<__main__.Taxon object at 0x...>]
print(orden.subcategorias)  # Output: [<__main__.Taxon object at 0x...>]
print(familia.subcategorias)  # Output: []