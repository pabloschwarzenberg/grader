class Auto:
    def __init__(self,capacidad_estanque,rendimiento):
        self.kilomentraje=0
        self.cuenta_kilometros=0
        self.capacidad_estanque=capacidad_estanque
        self.nivel_estanque=0
        self.rendimiento=rendimiento

    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros=0

    def andar(self,velocidad,tiempo_viaje):
        if velocidad*tiempo_viaje <= self.nivel_estanque*self.rendimiento:
            faltaron=0
        else:
            faltaron=(velocidad*tiempo_viaje)-(self.nivel_estanque*self.rendimiento)
        self.nivel_estanque=self.nivel_estanque-((velocidad*tiempo_viaje)/self.rendimiento)
        self.kilometraje=self.kilomentraje+(velocidad*tiempo_viaje)
        self.cuenta_kilometros=self.cuenta_kilometros+(velocidad*tiempo_viaje)
        return faltaron

    def autonomia(self):
        km=self.rendimiento*self.nivel_estanque
        return km

    def llenar_estanque(self,litros):
        if self.nivel_estanque+litros > self.capacidad_estanque:
            maximo=self.capacidad_estanque-self.nivel_estanque
            return (maximo,False)
        else:
            self.nivel_estanque=self.nivel_estanque+litros
            return(self.nivel_estanque,True)


if __name__ == "__main__":
    auto=Auto(100,12)
    vel=int(input("velocidad de viaje: "))
    t=int(input("Horas viaje: "))
    veces=vel*t/(100*12)
    veces=round(veces)