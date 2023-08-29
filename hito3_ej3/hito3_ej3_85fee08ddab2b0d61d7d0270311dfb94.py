class Taxon:
      def __init__(self,categoria,nombre):
          self.nombre=nombre
          self.categoria=categoria
          lista=[]
          self.subcategorias=lista
      def incluir(self,nuevo):
        
          self.subcategorias.append(nuevo)
      
      