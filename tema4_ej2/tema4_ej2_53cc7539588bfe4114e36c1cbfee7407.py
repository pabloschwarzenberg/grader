class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.capacidad_estanque=capacidad_estanque
        self.nivel_estanque=0
        self.rendimiento=rendimiento
        self.kilometraje=0
    def reiniciar_cuentakilometros(self):
        self.kilometraje=0
    def andar(self,velocidad,tiempo):
        distancia=velocidad*tiempo
        distancia_auto=self.rendimiento*self.nivel_estanque
        if distancia>distancia_auto:
            return distancia-distancia_auto
        else:
            self.nivel_estanque=self.nivel_estanque-(distancia*self.rendimiento)
            return 0
    def autonomia(self):
        autonomia=self.rendimiento*self.nivel_estanque
        return autonomia
    def llenar_estanque(self,litros):
        if self.nivel_estanque+litros>self.capacidad_estanque:
            return (self.capacidad_estanque,False)
        else:
            self.nivel_estanque=self.nivel_estanque+litros
        
    
if __name__ == "__main__":
    auto=Auto(100,12)
         