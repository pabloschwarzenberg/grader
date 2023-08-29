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
            distancia_restante = (self.nivel_estanque * self.rendimiento)
            self.nivel_estanque = 0
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


# Ejemplo de uso
auto = Auto(capacidad_estanque=100, rendimiento=12)

velocidad = 80  # km/h
tiempo_viaje = 6  # horas
distancia_viaje = velocidad * tiempo_viaje

litros_por_parada = 50

paradas_necesarias = 0
kilometros_faltantes = distancia_viaje

while kilometros_faltantes > 0:
    faltantes = auto.andar(velocidad, tiempo_viaje)
    if faltantes > 0:
        paradas_necesarias += 1
        litros_disponibles, _ = auto.llenar_estanque(litros_por_parada)
        distancia_recorrida = distancia_viaje - faltantes
        tiempo_viaje_restante = distancia_recorrida / velocidad
        tiempo_viaje = tiempo_viaje_restante
        kilometros_faltantes = faltantes
    else:
        break

print("Paradas necesarias:", paradas_necesarias)
