class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre
        self.subcategorias = []
aves = Taxon("Clase", "Aves")
orden = Taxon("Orden", "Passeriformes")
familia = Taxon("Familia", "Turdidae")

aves.subcategorias.append(orden)
orden.subcategorias.append(familia)
      