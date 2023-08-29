class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.kilometraje = 0
        self.cuenta_kilometros = 0
        self.capacidad_estanque = capacidad_estanque
        self.nivel_estanque = 0
        self.rendimiento = rendimiento

    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros = 0

    def andar(self, velocidad, tiempo):
        distancia = velocidad * tiempo
        consumo = distancia / self.rendimiento
        if consumo <= self.nivel_estanque:
            self.nivel_estanque -= consumo
            self.kilometraje += distancia
            self.cuenta_kilometros += distancia
            return 0
        else:
            distancia_recorrida = self.nivel_estanque * self.rendimiento
            self.nivel_estanque = 0
            self.kilometraje += distancia_recorrida
            self.cuenta_kilometros += distancia_recorrida
            return distancia - distancia_recorrida

    def autonomia(self):
        return self.nivel_estanque * self.rendimiento

    def llenar_estanque(self, litros):
        if litros <= self.capacidad_estanque - self.nivel_estanque:
            self.nivel_estanque += litros
            return (self.nivel_estanque, True)
        else:
            max_litros = self.capacidad_estanque - self.nivel_estanque
            return (max_litros, False)
