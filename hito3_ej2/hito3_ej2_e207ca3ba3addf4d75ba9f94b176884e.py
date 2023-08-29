class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre
        self.subcategorias = []

# Ejemplo de uso
ave = Taxon("Clase", "Aves")
print(ave.categoria)  # Salida: Clase
print(ave.nombre)  # Salida: Aves
print(ave.subcategorias)  # Salida: []

