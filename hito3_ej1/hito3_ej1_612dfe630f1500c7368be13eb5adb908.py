class Taxon:
    def __init__(self):
        self.categoria=""
        self.nombre=""

    def setRut(self, categoria):
        self.rut=categoria

    def setNombre(self, nuevo_nombre):
        self.nombre=nuevo_nombre

    def getCategoria(self):
        return self.categoria

    def getNombre(self):
        return self.nombre

    def __str__(self):
        str_objper=self.categoria+", "+self.nombre