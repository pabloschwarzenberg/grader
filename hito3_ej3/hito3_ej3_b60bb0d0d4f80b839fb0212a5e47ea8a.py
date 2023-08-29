class Taxon:
    def __init__(self,categoria,nombre):
        self.nombre=nombre
        self.categoria=categoria
        self.subcategorias=[]
    def incluir(self,taxon):
        self.subcategorias.append(taxon)
if __name__ == "__main__":
    ca=input("ingrese categoria:")
    no=input("ingrese nombre:")
    a=Taxon(ca,no)