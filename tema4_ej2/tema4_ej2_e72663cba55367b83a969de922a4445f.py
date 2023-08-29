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
            distancia_faltante = (litros_necesarios - self.nivel_estanque) * self.rendimiento
            self.kilometraje += distancia_faltante
            self.cuenta_kilometros += distancia_faltante
            self.nivel_estanque = 0
            return distancia_faltante

    def autonomia(self):
        return self.nivel_estanque * self.rendimiento

    def llenar_estanque(self, litros):
        if litros + self.nivel_estanque <= self.capacidad_estanque:
            self.nivel_estanque += litros
            return self.nivel_estanque, True
        else:
            max_litros = self.capacidad_estanque - self.nivel_estanque
            return max_litros, False


if __name__ == "__main__":
    auto = Auto(100, 12)
    distancia_total = 500  # Distancia total del viaje en kilómetros
    paradas = 0

    while distancia_total > 0:
        autonomia = auto.autonomia()
        if distancia_total <= autonomia:
            distancia_recorrida = distancia_total
            distancia_total = 0
        else:
            distancia_recorrida = autonomia
            distancia_total -= autonomia

        falta_combustible = auto.andar(100, distancia_recorrida)
        if falta_combustible > 0:
            paradas += 1
            litros_a_cargar, _ = auto.llenar_estanque(falta_combustible)
            auto.reiniciar_cuentakilometros()
            auto.andar(100, 0)  # Simular iniciar viaje nuevamente
            auto.andar(100, distancia_recorrida)
            auto.andar(100, 0)  # Simular continuar viaje después de cargar combustible

    print("Número de paradas para cargar combustible:", paradas)