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
            distancia_restante = (self.nivel_estanque * self.rendimiento) - self.cuenta_kilometros
            self.kilometraje += distancia_restante
            self.cuenta_kilometros += distancia_restante
            return distancia - distancia_restante

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
    distancia_viaje = 1000
    velocidad_viaje = 100
    tiempo_viaje = distancia_viaje / velocidad_viaje

    paradas = 0
    while distancia_viaje > 0:
        distancia_faltante = auto.andar(velocidad_viaje, tiempo_viaje)
        if distancia_faltante > 0:
            paradas += 1
        distancia_viaje = distancia_faltante

    print("Cantidad de paradas necesarias:", paradas)
