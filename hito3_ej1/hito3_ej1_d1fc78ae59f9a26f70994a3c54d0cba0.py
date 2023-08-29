class Taxon:
    def __init__(self,categoria,nombre):
        self.nombre=nombre
        self.categoria=categoria
        
    def __str__(self):
        return self.categoria+""+self.nombre