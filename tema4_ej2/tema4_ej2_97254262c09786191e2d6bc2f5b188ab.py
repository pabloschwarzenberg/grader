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

    def llenar_estanque(self, cantidad_litros):
        if cantidad_litros <= self.capacidad_estanque:
            self.nivel_estanque = cantidad_litros
            return self.nivel_estanque, True
        else:
            return self.capacidad_estanque, False


if __name__ == "__main__":
    auto = Auto(100, 12)

    distancia_viaje = 1000
    velocidad_viaje = 100
    tiempo_viaje = distancia_viaje / velocidad_viaje

    paradas_carga = 0
    distancia_restante = distancia_viaje

    while distancia_restante > 0:
        distancia_faltante = auto.andar(velocidad_viaje, tiempo_viaje)
        if distancia_faltante > 0:
            paradas_carga += 1
            distancia_restante -= distancia_faltante
        else:
            distancia_restante = 0

    print("Cantidad de paradas de carga:", paradas_carga)
