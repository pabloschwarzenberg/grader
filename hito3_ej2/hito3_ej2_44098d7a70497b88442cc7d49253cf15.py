class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre
        self.subcategorias = []

# Ejemplo de uso
ave = Taxon("Clase Aves", "Águila Real")
ave.subcategorias.append(Taxon("Orden Falconiformes", "Falconidae"))
ave.subcategorias.append(Taxon("Orden Falconiformes", "Accipitridae"))

print(ave.categoria)  # Salida: Clase Aves
print(ave.nombre)  # Salida: Águila Real
print(ave.subcategorias)  