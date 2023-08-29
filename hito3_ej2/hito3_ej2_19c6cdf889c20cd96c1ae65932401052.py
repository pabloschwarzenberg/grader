class Taxon:
	pass

class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre
        self.subcategorias = []

# Ejemplo de uso
ave = Taxon("Clase", "Aves")
print(ave.categoria)  # Output: Clase
print(ave.nombre)  # Output: Aves
print(ave.subcategorias)  # Output: []