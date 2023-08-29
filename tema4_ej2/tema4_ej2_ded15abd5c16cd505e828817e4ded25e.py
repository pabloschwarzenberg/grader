class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.kilometraje=0
        self.cuenta_kilometros=0
        self.capacidad_estanque=capacidad_estanque
        self.nivel_estanque=0
        self.rendimiento=rendimiento

    def reiniciar_cuentaKilometros(self):
        self.cuenta_kilometros=0

    def andar(self,velocidad,tiempo):
        if self.rendimiento*self.nivel_estanque>=velocidad*tiempo:
            self.nivel_estanque-=(velocidad*tiempo)/self.rendimiento
            self.kilometraje+=velocidad*tiempo
            self.cuenta_kilometros+=velocidad*tiempo
            return 0
        else:
            resto=(velocidad*tiempo)-(self.rendimiento*self.nivel_estanque)
            self.kilometraje+=self.rendimiento*self.nivel_estanque
            self.cuenta_kilometros+=self.rendimiento*self.nivel_estanque
            self.nivel_estanque=0
            return resto

    def autonomia(self):
        x=self.rendimiento*self.nivel_estanque
        return x

    def llenar_estanque(self,litros):
        if litros+self.nivel_estanque>self.capacidad_estanque:
            x=self.capacidad_estanque-(litros+self.nivel_estanque)
            y=False
            return x,y
        else:
            self.nivel_estanque+=litros+self.nivel_estanque
            x=litros+self.nivel_estanque
            y=True
            return x,y
    pass

if __name__ == "__main__":
    auto=Auto(100,12)
         