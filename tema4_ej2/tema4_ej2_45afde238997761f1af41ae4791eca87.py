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
        litros_necesarios = distancia / self.rendimiento

        if litros_necesarios <= self.nivel_estanque:
            self.kilometraje += distancia
            self.cuenta_kilometros += distancia
            self.nivel_estanque -= litros_necesarios
            return 0
        else:
            kilometros_faltantes = (litros_necesarios - self.nivel_estanque) * self.rendimiento
            self.kilometraje += distancia - kilometros_faltantes
            self.cuenta_kilometros += distancia - kilometros_faltantes
            self.nivel_estanque = 0
            return kilometros_faltantes

    def autonomia(self):
        return self.nivel_estanque * self.rendimiento

    def llenar_estanque(self, cantidad_litros):
        litros_faltantes = self.capacidad_estanque - self.nivel_estanque

        if cantidad_litros <= litros_faltantes:
            self.nivel_estanque += cantidad_litros
            return self.nivel_estanque, True
        else:
            return litros_faltantes, False


if __name__ == "__main__":
    auto = Auto(100, 12)

    distancia_total = 1000  # km
    velocidad_viaje = 100  # km/h
    tiempo_viaje = distancia_total / velocidad_viaje

    detenciones = 0

    while distancia_total > 0:
        faltante = auto.andar(velocidad_viaje, tiempo_viaje)
        if faltante > 0:
            detenciones += 1
            auto.llenar_estanque(auto.capacidad_estanque)
        distancia_total -= (velocidad_viaje * tiempo_viaje)

    print("Cantidad de veces que se debe detener a cargar combustible:", detenciones)

         