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
            self.nivel_estanque -= litros_consumidos
            self.kilometraje += distancia
            self.cuenta_kilometros += distancia
            return 0
        else:
            kilometros_faltantes = (self.nivel_estanque * self.rendimiento) - distancia
            self.kilometraje += (self.nivel_estanque * self.rendimiento)
            self.cuenta_kilometros += (self.nivel_estanque * self.rendimiento)
            self.nivel_estanque = 0
            return kilometros_faltantes

    def autonomia(self):
        return self.nivel_estanque * self.rendimiento

    def llenar_estanque(self, cantidad_litros):
        if cantidad_litros + self.nivel_estanque <= self.capacidad_estanque:
            self.nivel_estanque += cantidad_litros
            return self.nivel_estanque, True
        else:
            litros_maximos = self.capacidad_estanque - self.nivel_estanque
            return litros_maximos, False


if __name__ == "__main__":
    auto = Auto(100, 12)

    distancia_viaje = 1000  # Distancia del viaje en kilómetros
    velocidad_viaje = 80  # Velocidad promedio del viaje en km/h
    tiempo_viaje = distancia_viaje / velocidad_viaje  # Tiempo estimado del viaje en horas

    veces_cargar_combustible = 0

    while distancia_viaje > 0:
        autonomia = auto.autonomia()
        if autonomia < distancia_viaje:
            cargar_litros, exito = auto.llenar_estanque(auto.capacidad_estanque)
            veces_cargar_combustible += 1
            distancia_viaje -= (cargar_litros * auto.rendimiento)
        else:
            auto.andar(velocidad_viaje, tiempo_viaje)
            distancia_viaje = 0

    print("Número de veces que se debe cargar combustible:", veces_cargar_combustible)
