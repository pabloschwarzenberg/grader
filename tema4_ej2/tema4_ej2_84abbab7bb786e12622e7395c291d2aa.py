class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.kilometraje=0
        self.capacidad_estanque=capacidad_estanque
        self.nivel_estanque=0
        self.rendimiento=rendimiento
    def reiniciar_cuentakilometros(self):
        self.kilometraje=0
    def andar(self,velocidad,tiempo):
        distancia_total=velocidad*tiempo
        gasolina_consumida=distancia_total/self.rendimiento
        if gasolina_consumida<=self.nivel_estanque:
            self.nivel_estanque=self.nivel_estanque-gasolina_consumida
            return 0
        elif gasolina_consumida>self.nivel_estanque:
            distancia_recorrida=self.rendimiento*nivel_estanque
            distancia_faltante=distancia_total-distancia_faltante
            self.nivel_estanque=0
            return distancia_faltante

    def autonomia(self):
        distancia_recorrida=self.rendimiento*self.nivel_estanque
        return distancia_recorrida

    def llenar_estanque(self,litros):
        cuanto_llenar=self.capacidad_estanque-self.nivel_estanque
        if litros>cuanto_llenar:
            return (cuanto_llenar,False)
        else:
            self.nivel_estanque=self.nivel_estanque+litros
            return (self.nivel_estanque,True)
        
if __name__ == "__main__":
    auto=Auto(100,12)
         