class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.kilometraje = 0
        self.cuenta_kilometros = 0
        self.capacidad_estanque = capacidad_estanque
        self.nivel_estanque = 0
        self.rendimiento = rendimiento

    def reiniciar_cuenta_kilometros(self):
        self.cuenta_kilometros = 0

    def andar(self, velocidad, tiempo):
        distancia = velocidad * tiempo
        if distancia / self.rendimiento <= self.nivel_estanque:
            self.kilometraje += distancia
            self.cuenta_kilometros += distancia
            self.nivel_estanque -= distancia / self.rendimiento
            return 0
        if distancia / self.rendimiento > self.nivel_estanque:
            self.kilometraje += self.rendimiento * self.nivel_estanque
            self.cuenta_kilometros += self.rendimiento * self.nivel_estanque
            self.nivel_estanque -= 0
            por_recorrer= distancia - self.rendimiento * self.nivel_estanque
            return por_recorrer

    def autonomia(self):
        return self.rendimiento * self.nivel_estanque

    def llenar_estanque(self, litros):
        if litros <= (self.capacidad_estanque-self.nivel_estanque):
            self.nivel_estanque += litros
            return (self.nivel_estanque, True)
        elif litros > (self.capacidad_estanque-self.nivel_estanque):
            return ((self.capacidad_estanque-self.nivel_estanque), False)
