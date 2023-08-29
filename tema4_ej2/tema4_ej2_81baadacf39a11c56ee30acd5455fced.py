class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.maxcomb=capacidad_estanque
        self.ren=rendimiento
        self.kilo=0
        self.cuenta_kilo=0
        self.nivel_estanque=0

    def reiniciar_cuentakilometros(self):
        self.cuenta_kilo=0

    def andar(self,velocidad,tiempo):
        distancia= velocidad*tiempo
        self.cuenta_kilo+=distancia
        self.nivel_estanque-=distancia/self.ren
        if self.nivel_estanque>0:
            return 0
        else:
            return -(self.nivel_estanque*self.ren)

    def autonomia(self):
        kilometros=self.nivel_estanque*self.ren
        return kilometros

    def llenar_estanque(self,cantidad_litros):
        if cantidad_litros<=(self.maxcomb-self.nivel_estanque):
            self.nivel_estanque+=cantidad_litros
            return self.nivel_estanque, True
        else:
            return self.maxcomb-self.nivel_estanque, False

if __name__ == "__main__":
    auto=Auto(100,12)