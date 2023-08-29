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
        litros_consumidos = distancia / self.rendimiento
        if litros_consumidos <= self.nivel_estanque:
            self.kilometraje += distancia
            self.cuenta_kilometros += distancia
            self.nivel_estanque -= litros_consumidos
            return 0
        else:
            km_faltantes = (litros_consumidos - self.nivel_estanque) * self.rendimiento
            self.kilometraje += distancia - km_faltantes
            self.cuenta_kilometros += distancia - km_faltantes
            self.nivel_estanque = 0
            return km_faltantes

    def autonomia(self):
        return self.nivel_estanque * self.rendimiento

    def llenar_estanque(self, cantidad_litros):
        if cantidad_litros <= self.capacidad_estanque:
            self.nivel_estanque = cantidad_litros
            return self.nivel_estanque, True
        else:
            return self.capacidad_estanque, False


if __name__ == "__main__":
    auto = Auto(100, 12)
    distancia_viaje = 1000  # Distancia del viaje en kilómetros
    velocidad_viaje = 100  # Velocidad promedio del viaje en km/h
    tiempo_viaje = distancia_viaje / velocidad_viaje  # Tiempo del viaje en horas

    detenciones = 0  # Contador de detenciones para cargar combustible

    while distancia_viaje > 0:
        km_faltantes = auto.andar(velocidad_viaje, tiempo_viaje)
        if km_faltantes > 0:
            detenciones += 1
            auto.llenar_estanque(auto.capacidad_estanque)
            distancia_viaje -= km_faltantes
        else:
            distancia_viaje = 0

    print("Número de detenciones necesarias:", detenciones)

         