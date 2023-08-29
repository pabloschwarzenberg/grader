class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre
        self.subcategorias = []

# Ejemplo de uso
aves = Taxon("Clase", "Aves")
orden = Taxon("Orden", "Psittaciformes")
familia = Taxon("Familia", "Psittacidae")

aves.subcategorias.append(orden)
orden.subcategorias.append(familia)

print(aves.subcategorias)   # Salida: [<__main__.Taxon object at 0x...>]
print(orden.subcategorias)  # Salida: [<__main__.Taxon object at 0x...>]
print(familia.subcategorias) # Salida: []
