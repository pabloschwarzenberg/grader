class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre

# Ejemplo de uso
aves = Taxon("Clase", "Aves")
print(aves.categoria)  # "Clase"
print(aves.nombre)     # "Aves"

      