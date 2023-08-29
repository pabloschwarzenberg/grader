class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre
        self.subcategorias = []

    def incluir(self, taxon):
        self.subcategorias.append(taxon)

class Aves(Taxon):
    def __init__(self, nombre, especie, familia):
        super().__init__("Clase", nombre)
        self.especie = especie
        self.familia = familia

# Ejemplo de uso
clase_aves = Aves("Aves", "", "")
orden_falconiformes = Taxon("Orden", "Falconiformes")
clase_aves.incluir(orden_falconiformes)

print(clase_aves.subcategorias)  # Output: [<__main__.Taxon object at 0x00000123456789>]
