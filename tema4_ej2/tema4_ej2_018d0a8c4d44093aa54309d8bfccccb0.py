class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.kilometraje = 0
        self.cuenta_klometros = 0
        self.capacidad_estanque = capacidad_estanque
        self.nivel_estanque = 0
        self.rendimiento = rendimiento

    def reiniciar_cuentakilometros(self):
        self.cuenta_klometros = 0
    def andar(self, velocidad,tiempo):
        kilometros = velocidad*tiempo
        self.kilometraje = self.kilometraje + kilometros
        self.nivel_estanque = self.nivel_estanque - (kilometros//self.rendimiento)
        kilo = ((kilometros // self.rendimiento) - self.nivel_estanque)
        if kilo > 0:
            kilo = ((kilometros // self.rendimiento) - self.nivel_estanque)* self.rendimiento
        return kilo, self.rendimiento, self.nivel_estanque, self.nivel_estanque
    def autonomia(self):
        autonomia = self.nivel_estanque * self.rendimiento
        return autonomia
    def llenar_estanque(self,litros):
        if litros + self.nivel_estanque > self.capacidad_estanque:
            return (self.capacidad_estanque, False)
        elif litros + self.nivel_estanque <= self.capacidad_estanque:
            self.nivel_estanque = self.nivel_estanque + litros
            litros_auto= litros + self.nivel_estanque
            return (litros_auto, True)

         