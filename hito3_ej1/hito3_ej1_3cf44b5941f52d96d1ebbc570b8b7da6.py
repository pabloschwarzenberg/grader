# Ornitología 1
class Taxon:
    def __init__(self,c,n):
        self.categoria = c
        self.nombre = n

# Ornitología 2
class Taxon:
    def __init__(self,c,n):
        self.categoria = c
        self.nombre = n
        self.subcategorias = []


# Ornitología 3
class Taxon:
    def __init__(self,c,n):
        self.categoria = c
        self.nombre = n
        self.subcategorias = []
    def incluir(self,t):
        self.subcategorias.append(t) 
