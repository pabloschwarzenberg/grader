class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.capacidad_estanque = capacidad_estanque
        self.rendimiento = rendimiento
        self.kilometraje = 0
        self.cuenta_kilometros = 0
        self.nivel_estanque = 0

    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros = 0

    def andar(self,velocidad,tiempo):
        if (velocidad*tiempo) > (self.autonomia()):
            porrec = velocidad*tiempo - self.autonomia()
            self.nivel_estanque = 0
            self.kilometraje = self.kilometraje + (self.autonomia())
            self.cuenta_kilometros = self.cuenta_kilometros + (self.autonomia())
            return porrec

        else:
            self.nivel_estanque = self.nivel_estanque - ((velocidad*tiempo)/(self.rendimiento))
            self.kilometraje = self.kilometraje + (velocidad*tiempo)
            self.cuenta_kilometros = self.cuenta_kilometros + (velocidad*tiempo)
            return 0

    def autonomia(self):
        rec = self.rendimiento * self.nivel_estanque
        return rec

    def llenar_estanque(self,litros):
        if (self.nivel_estanque + litros) > self.capacidad_estanque:
            llenar = self.capacidad_estanque - self.nivel_estanque
            return llenar, False
        else:
            self.nivel_estanque = self.nivel_estanque + litros
            return self.nivel_estanque, True


if __name__ == "__main__":
    auto=Auto(100,12)
         