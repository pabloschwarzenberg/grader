class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.capacidad_estanque=capacidad_estanque
        self.rendimiento=rendimiento
        self.cuenta_kilometros=0
        self.nivel_estanque=0
        self.kilometraje=0
    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros=0
    def andar(self,velocidad,tiempo):
        distancia=velocidad*tiempo
        combus=float(distancia/self.rendimiento)
        if combus>self.nivel_estanque:
            self.kilometraje=self.kilometraje+self.nivel_estanque*self.rendimiento
            self.cuenta_kilometros=self.cuenta_kilometros+self.nivel_estanque*self.rendimiento
            self.nivel_estanque=0
            resta=distancia-self.nivel_estanque*self.rendimiento
            print(resta)
        else:
            self.kilometraje=self.kilometraje+distancia
            self.cuenta_kilometros=self.cuenta_kilometros+distancia
            self.nivel_estanque=self.nivel_estanque-combus
    def autonomia(self):
        auto=self.rendimiento*self.nivel_estanque
        return auto
    def llenar_estanque(self,litros):
        ya=self.nivel_estanque+litros
        if ya>self.capacidad_estanque:
            print (0,False)
        else:
            self.nivel_estanque=litros+self.nivel_estanque
            print (self.nivel_estanque,True)

if __name__ == "__main__":
    auto=Auto(100,12)
    print(auto)
