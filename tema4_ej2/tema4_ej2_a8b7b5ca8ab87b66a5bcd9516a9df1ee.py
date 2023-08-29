class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.kilometraje=0
        self.cuenta_kilometros=0
        self.capacidad_estanque=capacidad_estanque
        self.nivel_estanque=0
        self.rendimiento=rendimiento

    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros=0

    def andar(self, velocidad, tiempo_viaje):
        self.cuenta_kilometros=0
        kilometros_recorridos= velocidad*tiempo_viaje
        self.kilometraje=self.kilometraje+kilometros_recorridos
        gasto_estanque=kilometros_recorridos/self.rendimiento
        self.nivel_estanque=self.nivel_estanque-gasto_estanque

        if self.nivel_estanque < 0:
            kilometros_faltantes=self.nivel_estanque*-1*self.rendimiento
            self.nivel_estanque=0
            return kilometros_faltantes
        else:
            return 0
        
    def autonomia(self):
        autonomia=self.nivel_estanque*self.rendimiento
        return autonomia


    def llenar_estanque(self, cantidadLitros):
        self.nivel_estanque=cantidadLitros+self.nivel_estanque
        if self.nivel_estanque>self.capacidad_estanque:
            return (self.capacidad_estanque, False)
        else:
            return(self.nivel_estanque, True)
        
        

if __name__ == "__main__":
    auto=Auto(100,12)
         