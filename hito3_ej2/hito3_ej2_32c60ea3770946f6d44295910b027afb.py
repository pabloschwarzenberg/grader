class Taxon:
	pass
class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre
        self.subcategorias = []

# Ejemplo de uso
aves = Taxon("Clase", "Aves")
orden = Taxon("Orden", "Passeriformes")
familia = Taxon("Familia", "Turdidae")

aves.subcategorias.append(orden)
orden.subcategorias.append(familia)

print(aves.subcategorias)  # Salida: [<__main__.Taxon object at 0x7f0a55f89f40>]
print(orden.subcategorias)  # Salida: [<__main__.Taxon object at 0x7f0a55f89fd0>]
     