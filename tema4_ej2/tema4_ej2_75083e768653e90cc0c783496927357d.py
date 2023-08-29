class Auto:
    def __init__(self,estanque,rendimiento):
        self.kilometraje=0
        self.cuenta_kilometros=0
        self.capacidad_estanque=estanque
        self.nivel_estanque=0
        self.rendimiento=rendimiento
    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros=0
    def andar(self,vel,time):
        rec=time*vel
        self.cuenta_kilometros+=rec
        self.kilometraje+=rec
        gastado=rec/self.rendimiento
        if gastado>self.nivel_estanque:
            return rec-(gastado*self.rendimiento)
        else:
            self.nivel_estanque-=gastado
            return 0
    def autonomia(self):
        return self.rendimiento*self.nivel_estanque
    def llenar_estanque(self,litros):
        if litros > self.capacidad_estanque-self.nivel_estanque:
            return self.capacidad_estanque-self.nivel_estanque,False
        else:
            self.nivel_estanque+=litros
            return self.nivel_estanque,True

if __name__ == "__main__":
    auto=Auto(100,12)

         