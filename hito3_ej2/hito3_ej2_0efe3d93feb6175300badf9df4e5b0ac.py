class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre
        self.subcategorias = []

    def agregar_subcategoria(self, subcategoria):
        self.subcategorias.append(subcategoria)

# Ejemplo de uso
aves = Taxon("Clase", "Aves")
aves.agregar_subcategoria(Taxon("Orden", "Passeriformes"))
aves.agregar_subcategoria(Taxon("Orden", "Psittaciformes"))

mamiferos = Taxon("Clase", "Mamíferos")
mamiferos.agregar_subcategoria(Taxon("Orden", "Carnivora"))
mamiferos.agregar_subcategoria(Taxon("Orden", "Primates"))

print(aves.subcategorias)
print(mamiferos.subcategorias)
    