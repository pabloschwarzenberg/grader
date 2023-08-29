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
        distancia_recorrida = velocidad * tiempo
        litros_usados = distancia_recorrida / self.rendimiento
        if litros_usados > self.nivel_estanque:
            distancia_posible = self.nivel_estanque * self.rendimiento
            self.nivel_estanque = 0
            self.kilometraje += distancia_posible
            self.cuenta_kilometros += distancia_posible
            return distancia_recorrida - distancia_posible
        else:
            self.nivel_estanque -= litros_usados
            self.kilometraje += distancia_recorrida
            self.cuenta_kilometros += distancia_recorrida
            return 0

    def autonomia(self):
        return self.nivel_estanque * self.rendimiento

    def llenar_estanque(self, cantidad_litros):
        if cantidad_litros > (self.capacidad_estanque - self.nivel_estanque):
            return (self.capacidad_estanque - self.nivel_estanque), False
        else:
            self.nivel_estanque += cantidad_litros
            return (self.nivel_estanque), True

auto1 = Auto(100, 12)
