class Taxon:
    def __init__(self, categoria):
        self.categoria = categoria
        self.subcategorias = []

    def incluir(self, elemento):
        self.subcategorias.append(elemento)

# Ejemplo de uso
mi_taxon = Taxon("Reino animalia")
print(mi_taxon.subcategorias)  # Output: []

mi_taxon.incluir("Mamíferos")
mi_taxon.incluir("Aves")
mi_taxon.incluir("Reptiles")
print(mi_taxon.subcategorias)  # Output: ['Mamíferos', 'Aves', 'Reptiles']
