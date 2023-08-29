class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre
        self.subcategorias = []


ave = Taxon("Clase Aves", "Águila Real")
ave.subcategorias.append(Taxon("Orden Falconiformes", "Falconidae"))
ave.subcategorias.append(Taxon("Orden Falconiformes", "Accipitridae"))

print(ave.categoria)  
print(ave.nombre)  
print(ave.subcategorias)  
     