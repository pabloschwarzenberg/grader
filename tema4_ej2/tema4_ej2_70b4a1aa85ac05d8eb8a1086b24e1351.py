class Auto():
    def __init__(self, capacidad_estanque, rendimiento):
        self.kilometraje = 0
        self.cuenta_kilometros = 0
        self.capacidad_estanque = capacidad_estanque
        self.nivel_estanque = 0
        self.rendimiento = rendimiento

    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros = 0

    def andar(self, velocidad, tiempo_viaje):
        distancia = velocidad * tiempo_viaje
        self.nivel_estanque = self.nivel_estanque - (distancia / self.rendimiento)
        if (self.nivel_estanque < 0):
            kilometros_por_recorrer = distancia - (self.nivel_estanque * self.rendimiento)
            self.nivel_estanque = 0
            return kilometros_por_recorrer

        else:
            self.cuenta_kilometros = 0
            return self.cuenta_kilometros

    def autonomia(self):
        kilometros_puede_recorrer = self.nivel_estanque * self.rendimiento
        return kilometros_puede_recorrer

    def llenar_estanque(self, cantidad_litros):
        if (cantidad_litros > self.capacidad_estanque - self.nivel_estanque):
            return (self.capacidad_estanque, False)
        elif (cantidad_litros <= self.capacidad_estanque - self.nivel_estanque):
            self.nivel_estanque = self.nivel_estanque + cantidad_litros
            return (self.nivel_estanque, True)
if __name__ == "__main__":
    auto=Auto(100,12)
         