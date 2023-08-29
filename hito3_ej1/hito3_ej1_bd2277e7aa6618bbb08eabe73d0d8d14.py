class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre
        
class Aves(Taxon):
    def __init__(self, nombre, especie, habitat):
        super().__init__("Clase", nombre)
        self.especie = especie
        self.habitat = habitat

ave1 = Aves("Aguilucho", "Circus spilonotus", "Praderas")
ave2 = Aves("Colibrí", "Trochilidae", "Bosques tropicales")



      