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
print(ave.subcategorias)  # Salida: [<__main__.Taxon object at 0x00000123456789>, <__main__.Taxon object at 0x00000987654321>]
