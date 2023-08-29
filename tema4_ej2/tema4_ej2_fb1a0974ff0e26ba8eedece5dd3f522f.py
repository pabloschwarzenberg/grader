class Auto:
    def __init__(self,capacidad,rendimiento):
        self.kilometraje = 0
        self.cuenta_kilometros = 0
        self.capacidad_estanque = capacidad
        self.nivel_estanque = 0
        self.rendimiento = rendimiento

    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros = 0

    def andar(self,velocidad,tiempo):

        if 0 > self.autonomia() - velocidad*tiempo:
            self.nivel_estanque = 0
            self.kilometraje += velocidad*tiempo - self.autonomia()
            self.cuenta_kilometros += velocidad*tiempo - self.autonomia()
            return (self.autonomia() - velocidad*tiempo)*-1
        else:
            self.nivel_estanque -= (velocidad* tiempo)/self.rendimiento
            self.kilometraje += velocidad*tiempo
            self.cuenta_kilometros += velocidad*tiempo
            return 0

    def autonomia(self):
        return self.rendimiento * self.nivel_estanque

    def llenar_estanque(self,litros):
        if self.nivel_estanque + litros > self.capacidad_estanque:
            return (self.capacidad_estanque-self.nivel_estanque,False)

        else:
            self.nivel_estanque += litros
            return (self.nivel_estanque + litros,True)
        
        


        