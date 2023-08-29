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
            faltante = distancia - (self.nivel_estanque * self.rendimiento)
            self.kilometraje += (self.nivel_estanque * self.rendimiento)
            self.cuenta_kilometros += (self.nivel_estanque * self.rendimiento)
            self.nivel_estanque = 0
            return faltante

    def autonomia(self):
        return self.nivel_estanque * self.rendimiento

    def llenar_estanque(self, cantidad_litros):
        if cantidad_litros <= self.capacidad_estanque:
            self.nivel_estanque = cantidad_litros
            return self.nivel_estanque, True
        else:
            return self.capacidad_estanque, False


# Ejemplo de uso
if __name__ == "__main__":
    auto = Auto(100, 12)

    distancia_total = 1000  # Distancia total del viaje en kilómetros
    detenciones = 0

    while distancia_total > 0:
        autonomia_actual = auto.autonomia()
        if autonomia_actual < distancia_total:
            detenciones += 1
            distancia_recorrida = distancia_total - autonomia_actual
            auto.llenar_estanque(auto.capacidad_estanque)
            auto.reiniciar_cuentakilometros()
        else:
            auto.andar(distancia_total, 1)
            distancia_total = 0

    print("Número de detenciones en el viaje:", detenciones)
