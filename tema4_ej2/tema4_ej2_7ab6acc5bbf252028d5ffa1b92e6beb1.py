class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.capacidad_estanque = capacidad_estanque
        self.rendimiento = rendimiento
        self.cuenta_kilometros=0
        self.nivel_estanque=0
        self.kilometraje=0

    def reiniciar_cuenta_kilometros(self):
        self.cuenta_kilometros=0
    def andar(self,velocidad,tiempo):
        distancia_posible=velocidad*tiempo
        distancia_real=self.capacidad_estanque*self.rendimiento
        if distancia_posible<=distancia_real:
            self.nivel_estanque=self.nivel_estanque-distancia_posible/self.rendimiento
            self.kilometraje=self.kilometraje+distancia_posible
            self.cuenta_kilometros=self.cuenta_kilometros+distancia_posible
            return 0
        else:
            self.nivel_estanque=0
            self.kilometraje=self.kilometraje+distancia_real
            self.cuenta_kilometros = self.cuenta_kilometros + distancia_real
            return distancia_posible-distancia_real
    def autonomia(self):
        autonomia=self.nivel_estanque*self.rendimiento
        return autonomia
    def llenar_estanque(self,other):
        if other>self.capacidad_estanque-self.nivel_estanque:
            return(self.capacidad_estanque-self.nivel_estanque,False)
        else:
            self.nivel_estanque = self.nivel_estanque +other
            return (other,True)


if __name__ == "__main__":
    auto=Auto(100,12)
    auto.andar(100,13)
    print(auto.autonomia())
    print(auto.llenar_estanque(100))
    print(auto.autonomia())
         