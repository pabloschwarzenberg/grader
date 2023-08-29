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
        self.nivel_estanque = self.nivel_estanque - (distancia / self.rendimiento)
        self.kilometraje = self.kilometraje + distancia
        self.cuenta_kilometros = self.cuenta_kilometros + distancia
        if self.nivel_estanque > 0:
            return 0
        else:
            d_f = (-self.nivel_estanque * self.rendimiento)
            return d_f

    def autonomia(self):
        autonomia = self.nivel_estanque * self.rendimiento
        return autonomia

    def llenar_estanque(self, cantidad):
        if cantidad > self.capacidad_estanque:
            x=(self.capacidad_estanque, False)
            return x
        else:
            self.nivel_estanque = cantidad
            x=(cantidad, True)
            return x
if __name__ == "_main_":
    auto=Auto(100,12)