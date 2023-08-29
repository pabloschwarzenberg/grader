class Taxon:
    def __init__(self, categoria, nombre):
        self.categoria=categoria
        self.nombre=nombre
        ave=[]
        ave.append(categoria)
        ave.append(nombre)
        self.ave=ave
