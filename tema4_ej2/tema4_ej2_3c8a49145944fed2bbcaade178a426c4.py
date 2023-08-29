class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.capacidad_estanque= capacidad_estanque
        self.rendimiento= rendimiento
        self.nivel_estanque= 0
        self.cuenta_kilometros= 0
        self.kilometraje= 0

    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros= 0

    def andar(self, velocidad, tiempo):
        self.kilometros= velocidad*tiempo
        self.nivel_estanque-= self.kilometros/self.rendimiento
        self.cuenta_kilometros+= self.kilometros
        if self.nivel_estanque<0:
            a= -self.nivel_estanque
            return a
        else:
            return 0

    def autonomia(self):
        puede= self.nivel_estanque*self.rendimiento
        return puede
    def llenar_estanque(self, litros):
        if litros>self.capacidad_estanque:
            print("La maxima cantidad que puedes echar es de: "+str(self.capacidad_estanque))
            return False
        else:
            a=self.nivel_estanque= litros
            print(a)
            return True

if __name__ == "__main__":
    auto=Auto(100,12)
         