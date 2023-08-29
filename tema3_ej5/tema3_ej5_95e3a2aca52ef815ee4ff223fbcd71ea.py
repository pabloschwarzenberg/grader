import math
class Ciudad:
    def __init__(self, cordx, cordy):
        self.cordx = cordx
        self.cordy = cordy


    def camino (self, ciudad2):
        punto_medio = []
        coordenadas = []
        coord1 = []
        coord2 = []
        ciudad2 = Ciudad(cordx, cordy)
        punto_medio_x = (self.cordx+ciudad2.cordx)/2
        punto_medio_y = (self.cordy - ciudad2.cordy)/2
        punto_medio.append(punto_medio_x)
        punto_medio.append(punto_medio_y)
        coord1.append(self.cordx)
        coord1.append(self.cordy)
        coord2.append(ciudad2.cordx)
        coord2.append(ciudad2.cordy)
        coordenadas.append(coord1)
        coordenadas.append(punto_medio)
        coordenadas.append(coord2)
        return coordenadas


    def distancia (self, ciudad2):
        ciudad2 = Ciudad(cordx, cordy)
        distanciax = (self.cordx-ciudad2.cordx)**2
        distanciay = (self.cordy-ciudad2.cordy)**2
        distancia = (distanciax+distanciay)**(1/2)
        return distancia

if __name__ == "__main__":

    c1 = Ciudad(1,1)
    c2 = Ciudad(3,3)
    print(c1.camino(c2))
    print(c1.distancia(c2))