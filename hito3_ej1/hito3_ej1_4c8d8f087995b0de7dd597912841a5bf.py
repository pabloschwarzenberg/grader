class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre

# Ejemplo de uso
ave = Taxon("Clase", "Aves")
mamifero = Taxon("Clase", "Mamíferos")

# Imprimir los atributos de las instancias
print(ave.categoria, ave.nombre)         # Salida: Clase Aves
print(mamifero.categoria, mamifero.nombre)   # Salida: Clase Mamíferos
