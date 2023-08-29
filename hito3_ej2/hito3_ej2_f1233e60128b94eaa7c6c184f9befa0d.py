class Taxon:
    def __init__(self, categoria):
        self.categoria = categoria
        self.subcategorias = []

    def agregar_subcategoria(self, subcategoria):
        self.subcategorias.append(subcategoria)

    def __repr__(self):
        return self.categoria


if __name__ == "__main__":
    animalia = Taxon("Animalia")
    chordata = Taxon("Chordata")
    mammalia = Taxon("Mammalia")
    carnivora = Taxon("Carnivora")
    felidae = Taxon("Felidae")
    panthera = Taxon("Panthera")

    animalia.agregar_subcategoria(chordata)
    chordata.agregar_subcategoria(mammalia)
    mammalia.agregar_subcategoria(carnivora)
    carnivora.agregar_subcategoria(felidae)
    felidae.agregar_subcategoria(panthera)

    print(animalia)
    print(animalia.subcategorias)
    print(chordata.subcategorias)
    print(mammalia.subcategorias)
    print(carnivora.subcategorias)
    print(felidae.subcategorias)
