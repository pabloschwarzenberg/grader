"""
Para completar tu programa, agrega el método incluir, 
que recibe como parámetro un taxon y lo agrega en la lista de subcategorias de otro taxon. 
Por ejemplo, la Clase Aves incluye al Orden Falconiformes, 
que es donde se clasifican los Halcones.
"""
class Taxon:
    subcategorias=[]
    # constructor que inicialisa las variables de la calse
    def __init__(self,_categoria,_nombre):
        self.categoria=_categoria
        self.nombre=_nombre

    def imprimir(self):
        print("El nombre es: " + str(self.nombre))
        print("La categoria es: " + str(self.categoria))
        print("La subcategoria es: " + str(self.subcategorias))
    
    def incluir(self,_subcategorias):
        self.subcategorias.append(_subcategorias)