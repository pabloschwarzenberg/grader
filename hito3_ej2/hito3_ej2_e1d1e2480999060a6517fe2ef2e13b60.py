class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre
        self.subcategorias = []


reino = Taxon("Reino", "Animalia")
filo = Taxon("Filo", "Chordata")
clase = Taxon("Clase", "Aves")

reino.subcategorias.append(filo)
filo.subcategorias.append(clase)

print(reino.subcategorias)  
print(filo.subcategorias)  