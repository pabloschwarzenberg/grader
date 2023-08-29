class Taxon:
    def _init_(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre
        self.subcategorias = []
        pass
introducir = Taxon("Aves", "Aves")
print(introducir.categoria)
print(introducir.nombre)
print(introducir.subcategorias)