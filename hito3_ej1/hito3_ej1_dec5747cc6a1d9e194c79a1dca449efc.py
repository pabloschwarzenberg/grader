class Taxon:
    def init(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre
        self.subcategorias = []

    def incluir(self, taxon):
        self.subcategorias.append(taxon)
introducir = Taxon("Aves", "Aves")
print(introducir.categoria)  # Imprime "Aves"
print(introducir.nombre)  # Imprime "Aves"
print(introducir.subcategorias)  # Imprime []