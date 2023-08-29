class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre

class Aves(Taxon):
    def __init__(self, nombre, especie, familia):
        super().__init__("Clase", nombre)
        self.especie = especie
        self.familia = familia

ave = Aves("Gallus gallus domesticus", "Aves de corral", "Phasianidae")
print(ave.categoria)  # Output: Clase
print(ave.nombre)  # Output: Gallus gallus domesticus
print(ave.especie)  # Output: Aves de corral
print(ave.familia)  # Output: Phasianidae
