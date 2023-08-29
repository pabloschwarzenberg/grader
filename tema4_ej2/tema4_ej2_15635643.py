import math
class Auto:
    def __init__(self,capacidad_estanque,rendimiento):
        self.kilometraje=0
        self.cuenta_kilometros=0
        self.capacidad_estanque=capacidad_estanque
        self.nivel_estanque=0
        self.rendimiento=rendimiento
    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros=0
    def autonomia(self):
        autonom=self.nivel_estanque*self.rendimiento
        return autonom
    def llenar_estanque(self,litros):
        if self.nivel_estanque+litros>self.capacidad_estanque:
            return self.capacidad_estanque,False
        else:
            self.nivel_estanque+=litros
            return self.nivel_estanque,True
    def andar(self,velocidad,tiempo):
        gasto_combustible=velocidad*tiempo*(self.rendimiento**(-1))
        delta=self.nivel_estanque-gasto_combustible
        if delta>=0:
            self.nivel_estanque-=gasto_combustible
            self.kilometraje+=(velocidad*tiempo)
            self.cuenta_kilometros+=(velocidad*tiempo)
            return 0
        else:
            self.nivel_estanque=0
            self.cuenta_kilometros+=(self.nivel_estanque*self.rendimiento)
            self.kilometraje+=(self.nivel_estanque*self.rendimiento)
            faltaron=velocidad*tiempo-self.nivel_estanque*self.rendimiento
            return faltaron

if __name__ == "__main__":
    auto=Auto(100,12)
         