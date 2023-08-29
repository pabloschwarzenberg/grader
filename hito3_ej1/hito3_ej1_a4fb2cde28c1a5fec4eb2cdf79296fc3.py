# ornitologia 1

class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre

# Ejemplo de uso de la clase Taxon
ave = Taxon("Clase", "Aves")
print(ave.categoria)  # Imprime "Clase"
print(ave.nombre)     # Imprime "Aves"



# ornitologia 2

class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre
        self.subcategorias = []



# ornitologia 3


class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre
        self.subcategorias = []

    def incluir(self, taxon):
        self.subcategorias.append(taxon)