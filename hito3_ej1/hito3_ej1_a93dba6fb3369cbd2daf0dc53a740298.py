class Taxon:Paseriformes,Psittaciformes,Galliformes,Anseriformes,Falconiformes, Strigiformes, Struthioniformes,Columbiformes,  Piciformes
	pass
      def __init__(seft):
        seft.categoria=""
        seft.nombre=""
        
      def settaxon(seft,categoria):
        seft.categoria=categoria 
        
      def setnombre (self,nombre):
        self.nombre= nombre
       
      def gettaxon (self):
        return self.categoria
      def getnombre(self):
        return self.nombre
      def __str__(self):
        return self.categoria+" "+self.nombre