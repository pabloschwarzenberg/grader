class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre
        self.subcategorias = []

    def incluir(self, taxon):
        self.subcategorias.append(taxon)

ave = Taxon("Clase", "Aves")
orden = Taxon("Orden", "Falconiformes")
halcon = Taxon("Familia", "Halcones")

ave.incluir(orden)
orden.incluir(halcon)

print(ave.categoria, ave.nombre)  
for subcat_orden in ave.subcategorias:
    print(subcat_orden.categoria, subcat_orden.nombre)  
    for subcat_familia in subcat_orden.subcategorias:
        print(subcat_familia.categoria, subcat_familia.nombre) 