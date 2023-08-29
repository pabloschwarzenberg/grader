class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.capacidad_estanque = capacidad_estanque
        self.rendimiento = rendimiento
        self.kilometraje = 0
        self.cuenta_kilometros = 0
        self.nivel_estanque = 0

    def reiniciar_cuentakilometros(self, resetCK):
        if resetCK:
            self.cuenta_kilometros = 0
        return

    def andar(self, velocidad, tiempo_viaje):
        recorrido = velocidad * tiempo_viaje
        #print(recorrido)
        #print(toyota.nivel_estanque)
        if self.autonomia() >= recorrido:
            self.kilometraje += recorrido
            self.cuenta_kilometros += recorrido
            self.nivel_estanque -= recorrido / self.rendimiento
            #print(toyota.nivel_estanque)
            return 0
        else:
            return recorrido - self.autonomia()

    def autonomia(self):
        return self.rendimiento * self.nivel_estanque

    def llenar_estanque(self, uplift):
        if (uplift + self.nivel_estanque) > self.capacidad_estanque:
            max_uplift = self.capacidad_estanque - self.nivel_estanque
            return max_uplift, False
        else:
            self.nivel_estanque += uplift
            return self.nivel_estanque, True