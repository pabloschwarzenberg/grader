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

    def llenar_estanque(self, cantidad_litros):
        litros_permitidos = self.capacidad_estanque - self.nivel_estanque

        if cantidad_litros <= litros_permitidos:
            self.nivel_estanque += cantidad_litros
            return self.nivel_estanque, True
        else:
            return litros_permitidos, False


viaje = Auto(100, 12)

distancia_total = 500  # Distancia total del viaje en kilómetros
distancia_recorrida = 0
paradas = 0

while distancia_recorrida < distancia_total:
    distancia_faltante = distancia_total - distancia_recorrida
    autonomia = viaje.autonomia()

    if autonomia >= distancia_faltante:
        distancia_recorrida = distancia_total
    else:
        parada = distancia_faltante - autonomia
        distancia_recorrida += autonomia
        paradas += 1

        litros_para_parada, exito = viaje.llenar_estanque(parada)

        if not exito:
            distancia_recorrida -= (autonomia - litros_para_parada * viaje.rendimiento)
            break

print("Número de paradas de combustible necesarias:", paradas)