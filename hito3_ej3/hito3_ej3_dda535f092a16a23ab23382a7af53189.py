class Taxon:
    def __init__(self, nombre):
        self.nombre = nombre
        self.subcategorias = []
    def incluir(self, subcategoria):
        self.subcategorias.append(subcategoria)
clase_aves = Taxon("Clase Aves")
orden_falconiformes = Taxon("Orden Falconiformes")
clase_aves.incluir(orden_falconiformes)
print(clase_aves.subcategorias)