class Taxon:
    def __init__(self,categoria,nombre):
        self.subcategorias=[]
        self.categoria=categoria
        self.nombre=nombre
        return
            
    #¿No es necesario ponerlo como variable de la función?

    def incluir(self,taxon):
        subcategorias=self.subcategorias.append(taxon)
        return
      