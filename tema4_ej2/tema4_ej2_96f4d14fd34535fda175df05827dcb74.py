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
    
    def llenar_estanque(self, litros):
        if litros <= self.capacidad_estanque - self.nivel_estanque:
            self.nivel_estanque += litros
            return self.nivel_estanque, True
        else:
            max_litros = self.capacidad_estanque - self.nivel_estanque
            return max_litros, False


auto = Auto(capacidad_estanque=100, rendimiento=12)

distancia_total = 500
viaje_realizado = 0
paradas = 0

while viaje_realizado < distancia_total:
    autonomia_actual = auto.autonomia()

    if autonomia_actual <= 0:
        litros_necesarios = distancia_total - viaje_realizado
        litros_disponibles, exito = auto.llenar_estanque(litros_necesarios)

        if exito:
            viaje_realizado += litros_disponibles * auto.rendimiento
        else:
            print("No se puede completar el viaje. Parada forzada.")
            break

        paradas += 1
    else:
        distancia_restante = distancia_total - viaje_realizado

        if distancia_restante <= autonomia_actual:
            auto.andar(distancia_restante, 1)
            viaje_realizado += distancia_restante
        else:
            auto.andar(autonomia_actual, 1)
            viaje_realizado += autonomia_actual
            paradas += 1

print("Tendrás que detenerte a cargar combustible", paradas, "veces en el viaje.")
