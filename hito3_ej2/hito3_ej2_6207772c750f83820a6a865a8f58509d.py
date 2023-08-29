class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre
        self.subcategorias = []

# Ejemplo de uso
aves = Taxon("Clase", "Aves")
aves.subcategorias.append(Taxon("Orden", "Falconiformes"))
aves.subcategorias.append(Taxon("Orden", "Passeriformes"))

print(aves.categoria)  # Imprime "Clase"
print(aves.nombre)  # Imprime "Aves"
print(aves.subcategorias)  # Imprime la lista de subcategorias