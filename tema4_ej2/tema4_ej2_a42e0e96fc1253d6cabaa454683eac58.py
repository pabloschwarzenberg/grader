class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.kilometraje=0
        self.cuenta_kilometros=0
        self.capacidad_estanque=capacidad_estanque
        self.nivel_estanque=0 #menor o igual que la capacidad maxima
        self.rendimiento=rendimiento

    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros=0

    def andar(self,velocidad,tiempo_viaje):
        distancia=velocidad*tiempo_viaje
        self.kilometraje=distancia
        self.cuenta_kilometros=distancia
        self.nivel_estanque=self.nivel_estanque-distancia/self.rendimiento
        if self.nivel_estanque==0:
            return (distancia/rendimiento-distancia)

    def autonomia(self):
        kilometro_disponibles=self.rendimiento*self.nivel_estanque
        return kilometro_disponibles

    def llenar_estanque(self,cantidad_litros):
        if self.nivel_estanque+cantidad_litros>self.capacidad_estanque:
            tupla=(self.capacidad_estanque-self.nivel_estanque,False)
            return tupla
        else:
            self.nivel_estanque=self.nivel_estanque+cantidad_litros
            tupla=(self.nivel_estanque,True)
            return tupla
        
    
    
if __name__ == "__main__":
    auto=Auto(100,12)
    
         