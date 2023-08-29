class Auto:
    def __init__(self,capacidad_estanque,rendimiento):
        self.capacidad_estanque=capacidad_estanque
        self.rendimiento=rendimiento
        self.kilometraje=0
        self.cuenta_kilometros=0
        self.nivel_estanque=0
    def reiniciar_cuentakilometros(self,cuenta_kilometros):
        cuenta_kilometros=0
    def andar(self,velocidad,tiempo):
        kilometros=velocidad*tiempo
        self.kilometraje=self.kilometraje+kilometros
        self.cuenta_kilometros=self.cuenta_kilometros+kilometros
        litros=kilometros/self.rendimiento
        self.nivel_estanque=self.nivel_estanque-litros
    def autonomia(self):
        kilometros=self.nivel_estanque*self.rendimiento
        return kilometros
    def llenar_estanque(self,litros):
        if litros+self.nivel_estanque>self.capacidad_estanque:
            print(self.capacidad_estanque-self.nivel_estanque, False)
        else:
            self.nivel_estanque=self.nivel_estanque+litros
            print(self.nivel_estanque, True)

if __name__ == "__main__":
    auto=Auto(100,12)
         