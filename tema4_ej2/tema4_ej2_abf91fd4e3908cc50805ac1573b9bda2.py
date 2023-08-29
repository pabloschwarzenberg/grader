class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.kilometraje = 0
        self.cuenta_kilometros = 0
        self.capacidad_estanque = capacidad_estanque
        self.nivel_estanque = 0
        self.rendimiento = rendimiento
    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros = 0
        return self.cuenta_kilometros
    def andar(self,velocidad,tiempo):
        distancia_max = self.nivel_estanque*self.rendimiento
        distancia = velocidad*tiempo
        if distancia <= distancia_max:
            self.cuenta_kilometros += distancia
            self.kilometraje += distancia
            self.nivel_estanque -= distancia/self.rendimiento
            return 0
        return distancia-distancia_max
    def autonomia(self):
        return self.nivel_estanque*self.rendimiento
    def llenar_estanque(self,litros):
        if self.nivel_estanque+litros <= self.capacidad_estanque:
            self.nivel_estanque += litros
            return (self.nivel_estanque,True)
        return (self.capacidad_estanque,False)
    
    def cantidad_cargas(self,distancia_total):
        cargas = 1
        while distancia_total > 0:
            distancia_total -= self.capacidad_estanque*self.rendimiento
            cargas += 1

        return cargas
            
    

if __name__ == "__main__":
    auto=Auto(100,12)
         