class Auto:
    def __init__(self,capacidad_estanque,rendimiento):
        self.kilometraje=0
        self.cuenta_kilometros=0
        self.capacidad_estanque=capacidad_estanque
        self.nivel_estanque=0
        self.rendimiento=rendimiento

    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros=0

    def andar(self,velocidad,tiempo):
        distancia=velocidad*tiempo
        litros_usados=distancia/self.rendimiento
        if litros_usados<=self.nivel_estanque:
            self.nivel_estanque-=litros_usados
            self.kilometraje+=distancia
            self.cuenta_kilometros+=distancia
            return 0
        else:
            distancia_posible=self.nivel_estanque*self.rendimiento
            self.kilometraje+=distancia_posible
            self.cuenta_kilometros+=distancia_posible
            faltante=distancia-distancia_posible
            return faltante

    def autonomia(self):
        return self.nivel_estanque*self.rendimiento

    def llenar_estanque(self,litros):
        if litros>self.capacidad_estanque:
            return (self.capacidad_estanque,False)
        else:
            self.nivel_estanque=litros
            return (self.nivel_estanque,True)
         