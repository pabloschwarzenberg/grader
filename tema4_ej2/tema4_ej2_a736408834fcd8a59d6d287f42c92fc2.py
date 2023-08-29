class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.capacidad_estanque = capacidad_estanque
        self.rendimiento = rendimiento
        self.nivel_estanque = 0
        self.kilometraje = 0
        self.cuenta_kilometros = 0

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
            distancia_faltante = (self.nivel_estanque * self.rendimiento) - distancia
            self.kilometraje += distancia - distancia_faltante
            self.cuenta_kilometros += distancia - distancia_faltante
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


auto = Auto(capacidad_estanque=100, rendimiento=12)
viaje_distancia = 500  # Distancia total del viaje en kilómetros
paradas_carga = 0

while viaje_distancia > 0:
    autonomia_actual = auto.autonomia()
    if autonomia_actual < viaje_distancia:
        paradas_carga += 1
        auto.llenar_estanque(auto.capacidad_estanque)
        viaje_distancia -= autonomia_actual
    else:
        auto.andar(velocidad=100, tiempo=viaje_distancia / 100)
        viaje_distancia = 0

print("Tendrás que detenerte a cargar combustible", paradas_carga, "veces.")