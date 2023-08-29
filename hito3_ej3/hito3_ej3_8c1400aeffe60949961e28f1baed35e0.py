class Taxon:
    def __init__(self,categoria,nombre):
        self.categoria=str(categoria)
        self.nombre=str(nombre)
        self.subcategorias=[]

    def incluir(self,orden):
        self.subcategorias.append(orden)


      





