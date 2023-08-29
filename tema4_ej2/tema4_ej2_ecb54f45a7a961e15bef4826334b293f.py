class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.kilometraje = 0
        self.cuenta_kilometros = 0
        self.capacidad_estanque = capacidad_estanque
        self.nivel_estanque = 0
        self.rendimiento = rendimiento

    def reiniciar_cuentakilometros(self):
        self.kilometraje = 0

    def andar(self, velocidad, tiempo_de_viaje):
        self.nivel_estanque = (velocidad * tiempo_de_viaje)*5/self.rendimiento
        return self.nivel_estanque

    def autonomia(self):
        self.nivel_estanque = self.capacidad_estanque
        return int(self.capacidad_estanque*self.rendimiento)*0.6

    def llenar_estanque(self, litros):
        if self.nivel_estanque+litros > 100:
            return [str(100-self.nivel_estanque),False]
        if self.nivel_estanque+litros <= 100:
            self.nivel_estanque += litros
            return [str(self.nivel_estanque),True]


if __name__ == "__main__":
    auto=Auto(100,12)
         