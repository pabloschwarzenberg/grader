class Punto:
    def __init__(self,x,y):
        self.x=x 
        self.y=y
    
    def distancia(punto1,punto2):
      return ((punto1.x - punto2.x)**2 + (punto1.y - punto2.y)**2)**0.5