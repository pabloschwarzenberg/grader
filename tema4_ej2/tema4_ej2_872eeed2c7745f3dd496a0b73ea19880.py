class Auto:
    def __init__(self, capacidad_estanque, rendimiento):

        self.capacidad_estanque=capacidad_estanque
        self.rendimiento=rendimiento
        self.kilometraje=0
        self.cuenta_kilometros=0
        self.nivel_estanque=0

    def reiniciar_cuentakilometros(self):

        self.cuenta_kilometros=0

        return

    def andar(self,velocidad,tiempo_viaje):

        kilometros=velocidad*tiempo_viaje

        self.kilometraje=self.kilometraje+kilometros

        self.cuenta_kilometros=self.cuenta_kilometros+kilometros

        bencina=kilometros/self.rendimiento

        resta=self.nivel_estanque-bencina

        if resta>=0:

            self.nivel_estanque=resta

            return 0

        if resta<0:

            self.nivel_estanque=0

            falto=-(self.rendimiento*resta)

            return falto

    def autonomia(self):

        recorre=self.rendimiento*self.nivel_estanque

        return recorre 

    def llenar_estanque(self,litros):

        total=self.nivel_estanque+litros

        if total<=self.capacidad_estanque:

            self.nivel_estanque=total

            return (total,True)

        if total>self.nivel_estanque:

            maximo=self.capacidad_estanque-self.nivel_estanque

            return (maximo,False)

if __name__ == "__main__":
    auto=Auto(100,12)
         