class Taxon:
     def __init__(self,categoria,nombre):
        self.nombre=nombre
        self.categoria=categoria

     def imprimir(self):
        print("El nombre es: " + str(self.nombre))
        print("La categoria es: " + str(self.categoria))
      