class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.kilometraje = 0
        self.cuenta_kilometros = 0
        self.capacidad_estanque = capacidad_estanque
        self.nivel_estanque = 0
        self.rendimiento = rendimiento

    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros = 0

    def andar(self, velocidad, tiempo_de_viaje):
        distancia_maxima = self.nivel_estanque * self.rendimiento
        distancia_recorrida = velocidad * tiempo_de_viaje
        if distancia_recorrida > distancia_maxima:
            kilometros_restantes = distancia_recorrida - distancia_maxima
        else:
            kilometros_restantes = 0
            self.nivel_estanque -= distancia_recorrida / self.rendimiento
        return kilometros_restantes

    def autonomia(self):
        distancia_maxima = self.nivel_estanque * self.rendimiento
        return distancia_maxima

    def llenar_estanque(self, cantidad_de_litros):
        cantidad_total_de_litros = cantidad_de_litros + self.nivel_estanque
        if cantidad_total_de_litros > self.capacidad_estanque:
            llenado = False
            cantidad_total_de_litros = self.capacidad_estanque - self.nivel_estanque
        else:
            self.nivel_estanque = cantidad_total_de_litros
            llenado = True
        return cantidad_total_de_litros, llenado
            
