class Ciudad:
    def __init__(self,coordenada1,coordenada2):
        self.coordenada1 = coordenada1
        self.coordenada2 = coordenada2
        self.solucion = []
        self.solucion_parcial =[]
    def distancia(self,coordenada1,coordenada2):
        distancia = math.sqrt((coordenada1)**2+(coordenada2)**2)
        return distancia
    
    def camino(self,coordenada1,coordenada2):
        coordenada_candidata = coordenada1
        while bool(coordenada2 in self.solucion) == False:
            while self.distancia(coordenada_candidata,coordenada2) != 0:
                if x = self.distancia([coordenada1[0]+1,coordenada1[1]],coordenada2) < self.distancia(coordenada1,coordenada2):
                    coordenada_candidata[0] = coordenada_candidata[0]+1
                    self.solucion_parcial.append(coordenada_candidata)
                    
                elif x = self.distancia([coordenada1[0],coordenada1[1]+1],coordenada2) < self.distancia(coordenada1,coordenada2):
                    coordenada_candidata[1] = coordenada_candidata[1]+1
                    self.solucion_parcial.append(coordenada_candidata)
                    
                elif x = self.distancia([coordenada1[0]-1,coordenada1[1]],coordenada2) < self.distancia(coordenada1,coordenada2):
                    coordenada_candidata[0] = coordenada_candidata[0]-1
                    self.solucion_parcial.append(coordenada_candidata)

                    
                elif x = self.distancia([coordenada1[0],coordenada1[1]-1],coordenada2) < self.distancia(coordenada1,coordenada2):
                    coordenada_candidata[1] = coordenada_candidata[1] -1
                    self.solucion_parcial.append(coordenada_candidata)
        for elemento in self.solucion_parcial:
            if elemento != coordenada1:
                suma_distancias = suma_distancias + self.distancia(elemento,elemento-1)
        return self.solucion_parcial
city = Ciudad(input(),input())
if __name__ == "__main__":
  pass
         