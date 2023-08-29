class Taxon:
    def __init__(self,nombre,categoria):
        self.nombre = nombre
        self.categoria = categoria
    def incluir(self,subcategorias):
        self.subcategorias.append(subcategorias)

    def getNombre(self):
        return self.nombre

    def getCategoria(self):
        return self.categoria

categoria=input('ingrese catogoria: ')
nombre=input('ingrese nombre: ')
miPersona = Persona(nombre,categoria)
print("Nombre:",miPersona.getNombre())
print("Categoria:",miPersona.getCategoria())
      