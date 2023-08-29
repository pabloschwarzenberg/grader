class Taxon:
    def __init__(self, nombre):
        self.nombre = nombre
        self.subcategorias = []

    def incluir(self, taxon):
        self.subcategorias.append(taxon)

    def __str__(self):
        return self.nombre


# Ejemplo de uso
clase_aves = Taxon("Clase Aves")
orden_falconiformes = Taxon("Orden Falconiformes")
halcones = Taxon("Halcones")

clase_aves.incluir(orden_falconiformes)
orden_falconiformes.incluir(halcones)

print(clase_aves.subcategorias)  # Resultado: [Orden Falconiformes]
print(orden_falconiformes.subcategorias)  # Resultado: [Halcones]
