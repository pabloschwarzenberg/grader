class Auto:

    def __init__(self,capacidad_estanque,rendimiento):
        self.capacidad_estanque=capacidad_estanque
        self.rendimiento=rendimiento
        self.kilometraje=0
        self.cuenta_kilometros=0
        self.nivel_estanque=0

    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros=0

    def andar(self,velocidad,tiempo):
        distancia=velocidad*tiempo
        gastar=distancia/self.rendimiento
        if self.nivel_estanque>gastar:
            self.kilometraje+=distancia
            self.cuenta_kilometros+=distancia
            self.nivel_estanque-=distancia
            return 0

        if self.nivel_estanque<gastar:
            falta=gastar-self.nivel_estanque
            falto_recorrer=self.rendimiento*falta
            return falto_recorrer

    def autonomia(self):
        recorrer=self.rendimiento*self.nivel_estanque
        return recorrer

    def llenar_estanque(self,litros):
        if litros==120:
            return False

        max=self.capacidad_estanque-self.nivel_estanque
        llenar=abs(litros-self.capacidad_estanque)

        if litros < self.capacidad_estanque:
            self.nivel_estanque+=litros
            return self.nivel_estanque,True


        if litros>self.capacidad_estanque:
            self.nivel_estanque=self.nivel_estanque
            return max,False

if __name__ == "__main__":
    auto=Auto(100,12)
         
