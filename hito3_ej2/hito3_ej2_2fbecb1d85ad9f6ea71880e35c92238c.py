class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre
        self.subcategorias = []

introducir = Taxon("Aves", "Aves")
print(introducir.categoria)
print(introducir.nombre)
print(introducir.subcategorias)


