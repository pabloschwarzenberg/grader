class sub_categoria:
    def __init__(self, subcategoria):
        self.subcategoria=subcategoria
class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria=categoria
        self.nombre=nombre
        self.subcategorias= []
    def agregar_subcategoria(self,sub_categoria):
        self.subcategorias.append(sub_categoria)
 




      