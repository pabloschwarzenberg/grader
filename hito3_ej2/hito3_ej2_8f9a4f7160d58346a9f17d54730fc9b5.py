class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre
        self.subcategorias = []

if __name__ == "__main__":
    aves = Taxon("Clase", "Aves")
    mamiferos = Taxon("Clase", "Mamíferos")
    
    vertebrados = Taxon("Subfilo", "Vertebrados")
    invertebrados = Taxon("Subfilo", "Invertebrados")
    
    aves.subcategorias.append(vertebrados)
    aves.subcategorias.append(invertebrados)
    
    print("Categoría:", aves.categoria)
    print("Nombre:", aves.nombre)
    print("Subcategorías:", [subcategoria.nombre for subcategoria in aves.subcategorias])
