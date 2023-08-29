class Taxon:
    def __init__(self,categoria,nombre):
        self.categoria=categoria
        self.nombre=nombre
        self.aves=[]
    def agregar_ave(self,ave):
        self.aves.append(ave)
    def imprimir(self):
        print(self.aves)
          
aves=Taxon("Ave","Perro peluo")
aves.agregar_ave("Perro peluo")
aves.agregar_ave("Tifen Mayers")
aves.imprimir()
      