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
            self.nivel_estanque -= litros_necesarios
            self.kilometraje += distancia
            self.cuenta_kilometros += distancia
            return 0
        else:
            faltante = litros_necesarios - self.nivel_estanque
            self.kilometraje += self.nivel_estanque * self.rendimiento
            self.cuenta_kilometros += self.nivel_estanque * self.rendimiento
            self.nivel_estanque = 0
            return faltante

    def autonomia(self):
        return self.nivel_estanque * self.rendimiento

    def llenar_estanque(self, cantidad_litros):
        if cantidad_litros + self.nivel_estanque <= self.capacidad_estanque:
            self.nivel_estanque += cantidad_litros
            return self.nivel_estanque, True
        else:
            max_litros = self.capacidad_estanque - self.nivel_estanque
            return max_litros, False


if __name__ == "__main__":
    auto = Auto(100, 12)
    distancia_viaje = 500  # Distancia total del viaje en kilómetros
    velocidad_viaje = 80  # Velocidad promedio del viaje en km/h
    tiempo_viaje = distancia_viaje / velocidad_viaje  # Tiempo total del viaje en horas

    num_paradas = 0
    while distancia_viaje > 0:
        faltante = auto.andar(velocidad_viaje, tiempo_viaje)
        if faltante > 0:
            num_paradas += 1
            auto.llenar_estanque(faltante)
        distancia_viaje -= auto.cuenta_kilometros
        auto.reiniciar_cuentakilometros()

    print("Número de paradas requeridas:", num_paradas)
