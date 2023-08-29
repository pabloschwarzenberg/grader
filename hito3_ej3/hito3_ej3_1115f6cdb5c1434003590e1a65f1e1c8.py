class Taxon:
    def __init__(self,categoria,nombre,subcategorias = []):
        self.categoria = categoria
        self.nombre = nombre
        self.subcategorias = subcategorias
    def incluir(self, valor):
        return self.subcategorias.append(valor)
      