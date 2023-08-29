class Auto:
    def __init__(self,capacidad_estanque,rendimiento):
        self.capacidad_estanque = capacidad_estanque
        self.rendimiento = rendimiento
        self.kilometraje = 0
        self.cuenta_kilometros = 0
        self.nivel_estanque = 0
    
    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros = 0
    def andar(self,velocidad,tiempo_viaje):
        b = 0
        exito = 0
        distancia = velocidad*tiempo_viaje
        if self.nivel_estanque >= distancia/self.rendimiento:
            self.nivel_estanque = self.nivel_estanque - distancia/self.rendimiento
            self.kilometraje = self.kilometraje+distancia
            self.cuenta_kilometros = self.cuenta_kilometros + distancia
    
        else:
            exito = self.nivel_estanque*self.rendimiento
            self.kilometraje = self.kilometraje + exito
            self.cuenta_kilometros = self.kilometros + exito

        return exito
    def autonomia(self):
        autonomia = self.nivel_estanque * self.rendimiento
        return autonomia
    def llenar_estanque(self,litros):
        if self.capacidad_estanque > self.nivel_estanque + litros:
            self.nivel_estanque = self.nivel_estanque + litros
            return (self.nivel_estanque,True)
        else:
            diferencia = self.capacidad_estanque - self.nivel_estanque 
            return (diferencia,False)
        

        
        



if __name__ == "__main__":
    auto=Auto(100,12)
         