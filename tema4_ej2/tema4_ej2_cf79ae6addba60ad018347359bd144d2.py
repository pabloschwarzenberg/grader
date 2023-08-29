class Auto:
    def __init__(self, capacidad_estanque,rendimiento,kilometraje=0,cuenta_kilometros=0,nivel_estanque=0):
        self.capacidad_estanque=capacidad_estanque
        self.rendimiento=rendimiento
        self.kilometraje=kilometraje
        self.cuenta_kilometros=cuenta_kilometros
        self.nivel_estanque=nivel_estanque
    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros=0
    def andar(self,velocidad,tiempo):
        velocidad=velocidad/self.rendimiento
        distancia=velocidad*tiempo
        print(distancia)
        if (self.nivel_estanque-distancia)<0:
            a=self.nivel_estanque
            self.nivel_estanque=0
            return (distancia-a)*self.rendimiento
        else:
            self.nivel_estanque=self.nivel_estanque-distancia
            return "0"
    def autonomia(self):
        return self.nivel_estanque*self.rendimiento
    def llenar_estanque(self,litros):
        if litros>(self.capacidad_estanque-self.nivel_estanque):
            a=((self.capacidad_estanque-self.nivel_estanque),False)
            return a
        else:
            self.nivel_estanque=self.nivel_estanque+litros
            a=(self.nivel_estanque,True)
            return a

if __name__ == "__main__":
    auto=Auto(100,12)
    auto.reiniciar_cuentakilometros()
    print(auto.autonomia())
    print(auto.llenar_estanque(40))
    print(auto.llenar_estanque(70))
    print(auto.nivel_estanque)
    print(auto.autonomia())
    print(auto.andar(24,23))
    print(auto.nivel_estanque)