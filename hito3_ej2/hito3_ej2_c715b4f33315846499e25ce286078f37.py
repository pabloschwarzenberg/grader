class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre
        self.subcategorias = []

# Ejemplo de uso
aves = Taxon("Clase", "Aves")
mamiferos = Taxon("Clase", "Mamíferos")
vertebrados = Taxon("Subfilo", "Vertebrados")

aves.subcategorias.append(mamiferos)
aves.subcategorias.append(vertebrados)

print(aves.subcategorias)  # Imprime: [<__main__.Taxon object at 0x000001234567890>, <__main__.Taxon object at 0x000001234567891>]
