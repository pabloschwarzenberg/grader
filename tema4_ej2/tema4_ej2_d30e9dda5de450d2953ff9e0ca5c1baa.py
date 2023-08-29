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
            self.kilometraje += distancia - distancia_faltante
            self.cuenta_kilometros += distancia
            self.nivel_estanque = 0
            return distancia_faltante

    def autonomia(self):
        return self.nivel_estanque * self.rendimiento

    def llenar_estanque(self, cantidad_litros):
        litros_maximos = self.capacidad_estanque - self.nivel_estanque

        if cantidad_litros <= litros_maximos:
            self.nivel_estanque += cantidad_litros
            return self.nivel_estanque, True
        else:
            return litros_maximos, False
if __name__ == "__main__":
    auto = Auto(100, 12)
    distancia_viaje = 1000  # Distancia total del viaje en kilómetros
    velocidad_viaje = 80  # Velocidad promedio del viaje en km/h
    tiempo_viaje = distancia_viaje / velocidad_viaje  # Tiempo total del viaje en horas

    detenciones_carga = 0
    while distancia_viaje > 0:
        distancia_faltante = auto.andar(velocidad_viaje, tiempo_viaje)
        if distancia_faltante > 0:
            detenciones_carga += 1
            distancia_viaje -= distancia_faltante
        else:
            distancia_viaje = 0

    print("Cantidad de detenciones para cargar combustible:", detenciones_carga)