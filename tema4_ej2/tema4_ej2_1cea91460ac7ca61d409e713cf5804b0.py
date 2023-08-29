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
        self.kilometraje+=distancia
        self.cuenta_kilometros+=distancia
        self.nivel_estanque-=distancia/self.rendimiento
        if self.nivel_estanque<0:
            dist_por_recorrer=(-self.nivel_estanque)*self.rendimiento
            self.nivel_estanque=0
            return dist_por_recorrer
        else:
            return 0        
        

    def autonomia(self):
        kilometros=self.rendimiento*self.nivel_estanque
        return kilometros

    def llenar_estanque(self,litros):
        nuevo_estanque=litros+self.nivel_estanque
        if self.capacidad_estanque<nuevo_estanque:
            x=self.capacidad_estanque-self.nivel_estanque
            return (x,False)
        else:
            self.nivel_estanque+=litros
            return (self.nivel_estanque,True)

auto=Auto(100,12)
