class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre

# Ejemplo de uso
ave = Taxon("Aves", "Aguilucho")
print(ave.categoria)  # Output: Aves
print(ave.nombre)  # Output: Aguilucho
