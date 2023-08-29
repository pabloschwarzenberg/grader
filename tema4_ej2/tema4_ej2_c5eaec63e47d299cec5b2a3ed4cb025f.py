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
            distancia_faltante = (self.nivel_estanque * self.rendimiento) - self.cuenta_kilometros
            self.nivel_estanque = 0
            self.kilometraje += distancia_faltante
            self.cuenta_kilometros += distancia_faltante
            return distancia - distancia_faltante

    def autonomia(self):
        return self.nivel_estanque * self.rendimiento

    def llenar_estanque(self, cantidad_litros):
        if cantidad_litros <= self.capacidad_estanque:
            self.nivel_estanque = cantidad_litros
            return self.nivel_estanque, True
        else:
            return self.capacidad_estanque, False


#operacion
auto = Auto(100, 12)

#operacion
velocidad = 60  # km/h
tiempo = 5  # horas

distancia_total = velocidad * tiempo
kilometros_recorridos = 0
detenciones = 0

while kilometros_recorridos < distancia_total:
    if auto.nivel_estanque == 0:
        detenciones += 1
        litros_necesarios = (distancia_total - kilometros_recorridos) / auto.rendimiento
        auto.llenar_estanque(litros_necesarios)

    recorrido = auto.andar(velocidad, tiempo)
    kilometros_recorridos += recorrido

print(f"Se deben hacer {detenciones} detenciones para el viaje.")
