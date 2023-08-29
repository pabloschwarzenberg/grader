class Taxon:
    def __init__(self,categoria, nombre):
        self.categoria = categoria
        self.nombre = nombre

    def setCategoria(self, categoria):
        self.categoria = categoria
    def setNombre(self, nombre):
        self.nombre = nombre

    def getCategoria(self):
        return self.categoria
    def getNombre(self):
        return self.nombre
    
    def __str__(self):
        retorno = self.nombre + "," + str(self.categoria)
        return retorno

      