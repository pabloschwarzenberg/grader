class Taxon:
    def __init__(self,categoria,nombre):          ### Iniciacición de atributos
        self.categoria=categoria
        self.nombre=nombre
        self.subcategorias=[]
       
    def incluir(self,Taxon):
        self.subcategorias.append(Taxon)