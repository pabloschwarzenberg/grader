import math
class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.kilometraje=0
        self.cuenta_kilometros=0
        self.capacidad_estanque=capacidad_estanque
        self.nivel_estanque=0
        self.rendimiento=rendimiento
        pass
    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros=0

    def andar(self,velocidad,tiempo):
        kilometros=velocidad*tiempo
        self.kilometraje+=kilometros
        self.cuenta_kilometros+=kilometros
        self.nivel_estanque-=kilometros/self.rendimiento
        if (self.rendimiento*self.capacidad_estanque-kilometros)/self.rendimiento<= self.nivel_estanque:
            return 0
        else:
            return -(self.nivel_estanque*self.rendimiento)

    def autonomia(self):  #depende del rendimiento
        return self.nivel_estanque*self.rendimiento
    def llenar_estanque(self,litros_a_llenar):
        variable=self.capacidad_estanque-self.nivel_estanque
        if litros_a_llenar<=variable:
            self.nivel_estanque=self.nivel_estanque+litros_a_llenar
            return (self.nivel_estanque+litros_a_llenar,True)
        else:
            return (variable,False)
def kilometros(kilometros):
    variable=(kilometros*auto.capacidad_estanque)/(auto.capacidad_estanque*auto.rendimiento)
    variable2=(variable-auto.nivel_estanque)/auto.capacidad_estanque
    return math.ceil(variable2)




if __name__ == "__main__":
    auto=Auto(100,12)
    kilometros(1500)
    print(kilometros(1500))