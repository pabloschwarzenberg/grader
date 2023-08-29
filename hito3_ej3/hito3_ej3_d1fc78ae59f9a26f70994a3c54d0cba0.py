class Taxon:
    def __init__(self,categoria,nombre):
        self.nombre=nombre
        self.categoria=categoria
        self.subcategorias=[]        
    def __str__(self):
        return self.categoria+""+self.nombre+""+self.subcategoria
        
    def incluir(self,subcategoria):
        self.subcategorias.append(subcategoria)
    