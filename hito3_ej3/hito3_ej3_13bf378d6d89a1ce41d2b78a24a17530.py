class Taxon:
    def init(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre
        self.subcategorias = []

    def incluir(self, taxon):
        self.subcategorias.append(taxon)


clase_aves = Taxon("Clase", "Aves")
orden_falconiformes = Taxon("Orden", "Falconiformes")
familia_falconidae = Taxon("Familia", "Falconidae")


clase_aves.incluir(orden_falconiformes)
orden_falconiformes.incluir(familia_falconidae)


print(len(clase_aves.subcategorias))
print(orden_falconiformes.nombre)
print(familia_falconidae.categoria)