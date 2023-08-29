class Taxon:
	pass
class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre
        self.subcategorias = []  # Inicializar como lista vacía

    def incluir(self, taxon):
        self.subcategorias.append(taxon)

# Ejemplo de uso
aves = Taxon("Clase", "Aves")
print(aves.categoria)  # Salida: Clase
print(aves.nombre)     # Salida: Aves
print(aves.subcategorias)  # Salida: []

orden = Taxon("Orden", "Falconiformes")
aves.incluir(orden)
print(aves.subcategorias)  # Salida: [<__main__.Taxon object at 0x...>]
     