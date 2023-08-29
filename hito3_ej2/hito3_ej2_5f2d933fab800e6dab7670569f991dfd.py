class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre
        self.subcategorias = []

# Ejemplo de uso
aves = Taxon("Clase", "Aves")
orden = Taxon("Orden", "Passeriformes")
familia = Taxon("Familia", "Paridae")

aves.subcategorias.append(orden)
orden.subcategorias.append(familia)

print(aves.categoria)  # Imprime "Clase"
print(aves.nombre)  # Imprime "Aves"
print(aves.subcategorias)  # Imprime una lista con la instancia de orden

print(orden.categoria)  # Imprime "Orden"
print(orden.nombre)  # Imprime "Passeriformes"
print(orden.subcategorias)  # Imprime una lista con la instancia de familia
