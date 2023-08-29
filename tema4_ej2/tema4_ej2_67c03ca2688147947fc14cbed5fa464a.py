class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.kilometraje = 0
        self.cuenta_kilometros = 0
        self.capacidad_estanque = capacidad_estanque
        self.nivel_estanque = 0
        self.rendimiento = rendimiento

    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros = 0

    def andar(self, vel, t):
        dist = vel * t
        litros = dist / self.rendimiento
        if litros <= self.nivel_estanque:
            self.nivel_estanque -= litros
            self.kilometraje += dist
            self.cuenta_kilometros += dist
            return 0
        else:
            dist_posible = self.nivel_estanque * self.rendimiento
            self.kilometraje += dist_posible
            self.cuenta_kilometros += dist_posible
            falta = dist - dist_posible
            return falta

    def autonomia(self):
        return self.nivel_estanque * self.rendimiento

    def llenar_estanque(self, l):
        if l > self.capacidad_estanque:
            return (self.capacidad_estanque, False)
        else:
            self.nivel_estanque = l
            return (self.nivel_estanque, True)