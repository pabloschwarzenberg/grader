class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre

# Ejemplo de uso
ave = Taxon("Clase Aves", "Águila Real")
print(ave.categoria)  # Salida: Clase Aves
print(ave.nombre)  # Salida: Águila Real
