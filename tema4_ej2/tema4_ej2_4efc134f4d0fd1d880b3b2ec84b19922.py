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
            distancia_faltante = (self.nivel_estanque * self.rendimiento) - distancia
            self.nivel_estanque = 0
            self.kilometraje += distancia - distancia_faltante
            self.cuenta_kilometros += distancia - distancia_faltante
            return distancia_faltante

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

    velocidad_viaje = 80
    tiempo_viaje = 5
    distancia_total = velocidad_viaje * tiempo_viaje

    viajes_completos = distancia_total // (auto.rendimiento * auto.capacidad_estanque)
    distancia_restante = distancia_total % (auto.rendimiento * auto.capacidad_estanque)

    if distancia_restante > 0:
        viajes_completos += 1

    print("Tendrás que detenerte a cargar combustible", viajes_completos, "veces.")
