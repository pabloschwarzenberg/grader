class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre
        self.subcategorias = []

    def incluir(self, taxon):
        self.subcategorias.append(taxon)

if __name__ == "__main__":
    aves = Taxon("Clase", "Aves")
    falconiformes = Taxon("Orden", "Falconiformes")
    halcones = Taxon("Familia", "Halcones")
    
    aves.incluir(falconiformes)
    falconiformes.incluir(halcones)
    
    print("Categoría:", aves.categoria)
    print("Nombre:", aves.nombre)
    print("Subcategorías:", [subcategoria.nombre for subcategoria in aves.subcategorias])
