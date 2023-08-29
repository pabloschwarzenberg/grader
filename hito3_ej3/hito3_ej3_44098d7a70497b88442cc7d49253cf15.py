class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre
        self.subcategorias = []

    def incluir(self, taxon):
        self.subcategorias.append(taxon)

# Ejemplo de uso
clase_aves = Taxon("Clase Aves", "Aves")
orden_falconiformes = Taxon("Orden Falconiformes", "Falconiformes")
halcones = Taxon("Familia Falconidae", "Halcones")

clase_aves.incluir(orden_falconiformes)
orden_falconiformes.incluir(halcones)

print(clase_aves.categoria)  # Salida: Clase Aves
print(clase_aves.nombre)  # Salida: Aves
print(clase_aves.subcategorias)  

print(orden_falconiformes.categoria)  # Salida: Orden Falconiformes
print(orden_falconiformes.nombre)  # Salida: Falconiformes
print(orden_falconiformes.subcategorias)  

print(halcones.categoria)  # Salida: Familia Falconidae
print(halcones.nombre)  # Salida: Halcones
print(halcones.subcategorias)    