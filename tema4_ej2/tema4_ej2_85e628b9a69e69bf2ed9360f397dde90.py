class Auto:
    def __init__(self,ce,r):
        self.kilometraje=0
        self.cuenta_kilometros=0
        self.capacidad_estanque=ce
        self.nivel_estanque=0
        self.rendimiento=r

    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros=0

    def andar(self,v,t):
        self.reiniciar_cuentakilometros()
        do=v*t
        dq=self.nivel_estanque*self.rendimiento
        real=dq-do
        if real>=0:
            self.kilometraje+=do
            self.cuenta_kilometros=do
            self.nivel_estanque+=-do/self.rendimiento
            return 0
        else:
            self.kilometraje+=dq
            self.cuenta_kilometros=dq
            self.nivel_estanque+=-dq/self.rendimiento
            return abs(real)
    
    def autonomia(self):
        kilometros_restantes=self.nivel_estanque*self.rendimiento
        return kilometros_restantes

    def llenar_estanque(self,bencina):
        tope=self.capacidad_estanque-self.nivel_estanque-bencina
        if tope>=0:
            self.nivel_estanque+=bencina
            return self.nivel_estanque,True
        else:
            return abs(tope),False

if __name__ == "__main__":
    auto=Auto(100,12)
         