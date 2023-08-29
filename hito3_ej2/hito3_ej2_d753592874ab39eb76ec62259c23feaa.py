class Taxon:
    def __init__(self,categoria,nombre):          ### Iniciacición de atributos
        self.categoria=categoria
        self.nombre=nombre
        self.subcategorias=[]

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