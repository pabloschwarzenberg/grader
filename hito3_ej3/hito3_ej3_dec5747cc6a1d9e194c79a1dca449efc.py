class Taxon:
    def init(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre

Ejemplo de uso de la clase Taxon
ave = Taxon("Clase", "Aves")
print(ave.categoria)  # Imprime "Clase"
print(ave.nombre)  # Imprime "Aves"
class Taxon:
    def init(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre
        self.subcategorias = []
        pass
introducir = Taxon("Aves", "Aves")
print(introducir.categoria)
print(introducir.nombre)
print(introducir.subcategorias)
class Taxon:
    def init(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre
        self.subcategorias = []

    def incluir(self, taxon):
        self.subcategorias.append(taxon)