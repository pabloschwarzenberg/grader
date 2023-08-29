class Taxon:
    def __init__(self,categoria,nombre):          ### Iniciacición de atributos
        self.categoria=categoria
        self.nombre=nombre

    def setCategoria(self,categoria):
        self.categoria=categoria
    def setNombre(self,nombre):
        self.nombre=nombre

    def getCategoria(self):
        return self.categoria
    def getNombre(self):
        return self.nombre

    def __str__(self):
        return self.categoria + " " + self.nombre
        
#categoria_1=input("Ingrese categoría: ")
#nombre_1=input("Ingrese nombre: ")
#p1=Taxon(categoria_1,nombre_1)
#print(p1)
    