class Taxon:
    categoria = []
    nombre = []
    subcategorias = []

    def __init__(self,categoria,nombre):
        self.categoria = categoria
        self.nombre = nombre

    def func(self,subcategorias):
        self.subcategorias = subcategorias

    def incluir_c(self):
        return self.categoria

    def incluir_n(self):
        return self.nombre

    def incluir(self):
        return self.subcategorias


    def __str__(self):
        return f"{self.categoria} {self.nombre} {self.subcategorias} kms."


a = Taxon()
a.categoria("bipedo")
a.nombres("Alcon")
a.subcategorias("Falconiformes")
print(a)
        
