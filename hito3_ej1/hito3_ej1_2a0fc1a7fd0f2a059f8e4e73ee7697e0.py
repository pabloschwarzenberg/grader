class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre
        
# Creación de un objeto Taxon con categoría "Aves" y nombre "Falco peregrinus"
taxon1 = Taxon("Aves", "Falco peregrinus")

# Acceso a los atributos del objeto Taxon
print(taxon1.categoria)  # salida: Aves
print(taxon1.nombre)     # salida: Falco peregrinus