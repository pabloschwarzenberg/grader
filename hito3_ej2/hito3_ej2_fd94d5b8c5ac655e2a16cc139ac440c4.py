class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre
        self.subcategorias = []
class Animal:
    def __init__(self, nombre):
        self.taxon = Taxon("Reino", "Animal")
        self.subcategorias = []
        self.nombre = nombre

reino_animal = Animal("Reino Animal")
clase_aves = Animal("Clase Aves")
orden_passeriformes = Animal("Orden Passeriformes")

reino_animal.subcategorias.append(clase_aves)
clase_aves.subcategorias.append(orden_passeriformes)

      