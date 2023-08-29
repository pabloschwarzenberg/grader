class Auto():
    def __init__(self,capacidad_estanque,rendimiento):
        self.kilometraje=0
        self.cuenta_kilometros=0
        self.capacidad=capacidad_estanque
        self.nivel_estanque=0
        self.rendimiento=rendimiento
    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros=0
    def andar(self, velocidad, tiempo):
        self.kilometraje+=velocidad*tiempo
        self.cuenta_kilometros+=velocidad*tiempo
        if self.nivel_estanque-(velocidad*tiempo)/self.rendimiento<0:
            return (velocidad*tiempo)-(self.rendimiento*self.nivel_estanque)
        else:
            self.nivel_estanque-=(velocidad*tiempo)/self.rendimiento
            return 0
    def autonomia(self):
        return (self.rendimiento*self.nivel_estanque)
    def llenar_estanque(self, litros):
        if litros>int(self.capacidad)-int(self.nivel_estanque):
            return (self.capacidad-self.nivel_estanque, False)
        else:
            self.nivel_estanque+=litros
            return (self.nivel_estanque, True)

if __name__ == "__main__":
    auto=Auto(100,12)
         