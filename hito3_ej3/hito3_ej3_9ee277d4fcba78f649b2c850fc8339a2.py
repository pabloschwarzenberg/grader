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

aves.incluir(orden)

print(aves.subcategorias)  # Salida: [<__main__.Taxon object at 0x...>]
