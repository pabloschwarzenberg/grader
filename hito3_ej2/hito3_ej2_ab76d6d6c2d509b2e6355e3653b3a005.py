class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre
        self.subcategorias = []


ave = Taxon("Clase", "Aves")
print(ave.categoria)  
print(ave.nombre) 
print(ave.subcategorias)