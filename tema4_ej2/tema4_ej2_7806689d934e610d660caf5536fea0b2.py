import math
class Auto:
    def __init__(self,capacidad_estanque,rendimiento,kilometraje=0,cuenta_kilometros=0,nivel_estanque=0):
        self.capacidad_estanque=capacidad_estanque
        self.rendimiento=rendimiento

        self.kilometraje=kilometraje
        self.cuenta_kilometros=cuenta_kilometros
        self.nivel_estanque=nivel_estanque
    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros=0
    def andar(self,velocidad,tiempo):
        distancia=velocidad*tiempo
        litros_gastados=distancia/self.rendimiento
        litros=(self.nivel_estanque)-(litros_gastados)
        if litros<0:
            km=(math.fabs(litros))*(self.rendimiento)
            return "faltaron",km,"km"
        elif litros==0 or litros>0:
            self.nivel_estanque=(litros)
            return "0"
    def autonomia(self):
        autonomia=(self.nivel_estanque)*(self.rendimiento)
        return autonomia
    def llenar_estanque(self,lt):
        self.nivel_estanque=lt+self.nivel_estanque
        if self.nivel_estanque>self.capacidad_estanque:
            self.nivel_estanque=self.nivel_estanque-lt
            maxima=math.fabs((self.capacidad_estanque)-(self.nivel_estanque))
            return tuple([maxima,False])
        elif self.nivel_estanque<self.capacidad_estanque or self.nivel_estanque==self.capacidad_estanque:
            return tuple([self.nivel_estanque,True])
        
if __name__ == "__main__":
    auto=Auto(100,12)
    print(auto.llenar_estanque(70))
    print(auto.andar(60,4))
    print(auto.llenar_estanque(10))
    print(auto.autonomia())
    print(auto.nivel_estanque)
