class Taxon:
    def __init__(self,categoria,nombre):
        self.categoria=categoria
        self.nombre=nombre
        self.subcategorias=[]
    def __str__(self):
        return "categoria "+str(categoria)+","+" tipo:"+str(nombre)
      