class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre
        self.subcategorias = []

# Ejemplo de uso
ave = Taxon("Clase", "Aves")
ave.subcategorias.append(Taxon("Orden", "Falconiformes"))
ave.subcategorias.append(Taxon("Orden", "Psittaciformes"))

print(ave.categoria)  # Salida: Clase
print(ave.nombre)  # Salida: Aves
print(len(ave.subcategorias))  # Salida: 2
print(ave.subcategorias[0].nombre)  # Salida: Falconiformes
print(ave.subcategorias[1].nombre)  # Salida: Psittaciformes
