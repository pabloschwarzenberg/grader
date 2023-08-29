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
            distancia_faltante = (self.nivel_estanque * self.rendimiento) - distancia
            self.kilometraje += (distancia - distancia_faltante)
            self.cuenta_kilometros += (distancia - distancia_faltante)
            self.nivel_estanque = 0
            return distancia_faltante

    def autonomia(self):
        return self.nivel_estanque * self.rendimiento

    def llenar_estanque(self, cantidad_litros):
        if cantidad_litros > self.capacidad_estanque:
            return self.capacidad_estanque, False
        else:
            self.nivel_estanque = cantidad_litros
            return self.nivel_estanque, True


# Ejemplo de uso
auto = Auto(100, 12)

velocidad = 60  # km/h
tiempo = 4  # horas

viaje_total = 800  # km
viaje_realizado = 0  # km
detenciones = 0

while viaje_realizado < viaje_total:
    distancia_faltante = auto.andar(velocidad, tiempo)
    viaje_realizado += (velocidad * tiempo)

    if distancia_faltante > 0:
        detenciones += 1
        litros_necesarios = distancia_faltante / auto.rendimiento
        auto.llenar_estanque(litros_necesarios)

print(f"Detenciones necesarias: {detenciones}")
