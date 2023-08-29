class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre
        self.subcategorias = []

#Ejemplo de uso
aves = Taxon("Clase", "Aves")
orden = Taxon("Orden", "Falconiformes")
familia = Taxon("Familia", "Accipitridae")

aves.subcategorias.append(orden)
orden.subcategorias.append(familia)

print(aves.categoria)  #Output: Clase
print(aves.nombre)  #Output: Aves
print(aves.subcategorias)  #Output: [<__main__.Taxon object at 0x...>]

print(orden.categoria)  #Output: Orden
print(orden.nombre)  #Output: Falconiformes
print(orden.subcategorias)  #Output: [<__main__.Taxon object at 0x...>]

print(familia.categoria)  #Output: Familia
print(familia.nombre)  #Output: Accipitridae
print(familia.subcategorias)  #Output: []
