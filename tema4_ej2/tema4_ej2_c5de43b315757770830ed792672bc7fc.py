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
            distancia_recorrida = self.nivel_estanque * self.rendimiento
            self.kilometraje += distancia_recorrida
            self.cuenta_kilometros += distancia_recorrida
            return distancia - distancia_recorrida

    def autonomia(self):
        return self.nivel_estanque * self.rendimiento

    def llenar_estanque(self, litros):
        if litros <= self.capacidad_estanque - self.nivel_estanque:
            self.nivel_estanque += litros
            return self.nivel_estanque, True
        else:
            max_litros = self.capacidad_estanque - self.nivel_estanque
            return max_litros, False

if __name__ == "__main__":
    auto = Auto(100, 12)

    distancia_viaje = 500
    velocidad_viaje = 80
    tiempo_viaje = distancia_viaje / velocidad_viaje

    paradas_carga = 0

    while distancia_viaje > 0:
        resultado = auto.andar(velocidad_viaje, tiempo_viaje)
        if resultado > 0:
            distancia_viaje = resultado
            paradas_carga += 1
        else:
            distancia_viaje = 0

    print("Número de paradas de carga:", paradas_carga)

         