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
            distancia_recorrida = self.nivel_estanque * self.rendimiento
            self.kilometraje += distancia_recorrida
            self.cuenta_kilometros += distancia_recorrida
            self.nivel_estanque = 0
            return distancia - distancia_recorrida

    def autonomia(self):
        return self.nivel_estanque * self.rendimiento

    def llenar_estanque(self, cantidad_litros):
        if cantidad_litros <= self.capacidad_estanque - self.nivel_estanque:
            self.nivel_estanque += cantidad_litros
            return self.nivel_estanque, True
        else:
            max_litros = self.capacidad_estanque - self.nivel_estanque
            return max_litros, False

# Ejemplo de uso
auto = Auto(100, 12)  # Capacidad de estanque: 100 litros, rendimiento: 12 km/l

velocidad_viaje = 80  # km/h
tiempo_viaje = 6  # horas

distancia_total = velocidad_viaje * tiempo_viaje
viajes_realizados = 0

while distancia_total > 0:
    faltante = auto.andar(velocidad_viaje, tiempo_viaje)
    if faltante > 0:
        viajes_realizados += 1
        print("Debes detenerte a cargar combustible. Faltaron por recorrer:", faltante, "kilómetros")
        litros_para_llenar, exito = auto.llenar_estanque(auto.capacidad_estanque)
        if exito:
            print("Llenaste el estanque con", litros_para_llenar, "litros")
        else:
            print("Solo puedes llenar hasta", litros_para_llenar, "litros")
    else:
        print("El viaje se completó sin necesidad de cargar combustible")
    distancia_total -= (velocidad_viaje * tiempo_viaje)

print("Total de viajes realizados:", viajes_realizados)

         