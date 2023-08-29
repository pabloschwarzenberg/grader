class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre
        self.subcategorias = []

# Crear un objeto Taxon para la Clase Aves
aves = Taxon("Clase", "Aves")

# Acceder a los atributos
print(aves.categoria)       # Salida: Clase
print(aves.nombre)          # Salida: Aves
print(aves.subcategorias)   # Salida: []
