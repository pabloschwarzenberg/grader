class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre
        self.subcategorias = []

ave = Taxon("Clase", "Aves")
orden = Taxon("Orden", "Passeriformes")
familia = Taxon("Familia", "Turdidae")

ave.subcategorias.append(orden)
orden.subcategorias.append(familia)

print(ave.categoria, ave.nombre)  
print(orden.categoria, orden.nombre)  
print(familia.categoria, familia.nombre)