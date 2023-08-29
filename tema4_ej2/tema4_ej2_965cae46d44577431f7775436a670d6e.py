class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.kilometraje = 0
        self.cuenta_kilometros = 0
        self.capacidad_estanque = capacidad_estanque
        self.nivel_estanque = 0
        self.rendimiento = rendimiento

    def reiniciar_cuenta_kilometros(self):
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
            distancia_faltante = (self.nivel_estanque * self.rendimiento) - distancia
            return distancia_faltante

    def autonomia(self):
        return self.nivel_estanque * self.rendimiento

    def llenar_estanque(self, cantidad_litros):
        if cantidad_litros + self.nivel_estanque > self.capacidad_estanque:
            max_litros = self.capacidad_estanque - self.nivel_estanque
            return max_litros, False
        else:
            self.nivel_estanque += cantidad_litros
            return self.nivel_estanque, True


auto = Auto(70, 7)

distancia_total = 500
velocidad_viaje = 80
tiempo_viaje = distancia_total / velocidad_viaje

num_paradas = 0
distancia_recorrida = 0

while distancia_recorrida < distancia_total:
    distancia_faltante = auto.andar(velocidad_viaje, tiempo_viaje)
    if distancia_faltante > 0:
        num_paradas += 1
        distancia_recorrida += distancia_total - distancia_faltante
    else:
        distancia_recorrida += distancia_total

print("Número de paradas necesarias:", num_paradas)