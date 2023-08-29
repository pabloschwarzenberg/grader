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
            distancia_faltante = (litros_necesarios - self.nivel_estanque) * self.rendimiento
            self.kilometraje += distancia - distancia_faltante
            self.cuenta_kilometros += distancia - distancia_faltante
            self.nivel_estanque = 0
            return distancia_faltante

    def autonomia(self):
        return self.nivel_estanque * self.rendimiento

    def llenar_estanque(self, litros):
        if litros > self.capacidad_estanque:
            return (self.capacidad_estanque, False)
        else:
            self.nivel_estanque = litros
            return (self.nivel_estanque, True)


def calcular_paradas_viaje(auto, distancia_viaje):
    paradas = 0
    distancia_recorrida = 0

    while distancia_recorrida < distancia_viaje:
        distancia_faltante = distancia_viaje - distancia_recorrida
        autonomia_actual = auto.autonomia()

        if autonomia_actual >= distancia_faltante:
            distancia_recorrida += distancia_faltante
        else:
            paradas += 1
            litros_necesarios = distancia_faltante / auto.rendimiento
            auto.llenar_estanque(litros_necesarios)

    return paradas


# Crear instancia del auto
auto = Auto(100, 12)

# Calcular paradas en un viaje de 1000 km
distancia_viaje = 1000
paradas = calcular_paradas_viaje(auto, distancia_viaje)

print("Número de paradas necesarias en un viaje de", distancia_viaje, "km:", paradas)

       

if __name__ == "__main__":
    auto=Auto(100,12)
         