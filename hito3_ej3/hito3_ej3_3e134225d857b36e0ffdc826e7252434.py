class Taxon:
    subcategorias = []
    def __init__(self, categoria, nombre):
    
        self.categoria = 'Clase'
        self.nombre = 'Aves'
        self.subcategorias = []
        
    def incluir(self, subcategorias):
        
        self.subcategorias.append(subcategorias)
