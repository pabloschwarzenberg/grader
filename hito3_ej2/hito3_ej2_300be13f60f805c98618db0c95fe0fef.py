class Taxon:
	pass
class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre
        self.subcategorias = []

# Ejemplo de uso
clase_aves = Taxon("Clase", "Aves")
orden_passeriformes = Taxon("Orden", "Passeriformes")
familia_turdidae = Taxon("Familia", "Turdidae")

clase_aves.subcategorias.append(orden_passeriformes)
orden_passeriformes.subcategorias.append(familia_turdidae)

print(clase_aves.subcategorias)  # Imprime: [<__main__.Taxon object at 0x...>]
print(orden_passeriformes.subcategorias)  # Imprime: [<__main__.Taxon object at 0x...>]
     