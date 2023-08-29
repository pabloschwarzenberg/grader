class Auto:
    def __init__(self,capacidad,rendimiento):
        self.capacidad=capacidad
        self.rendimiento=rendimiento
        self.kilometraje=0
        self.cuenta_kilometros=0
        self.nivel_estanque=0


    def reiniciar(self):
        self.cuenta_kilometros=0
        return self.cuenta_kilometros

    def andar(self,velocidad,tiempo):
        self.velocidad=velocidad
        self.tiempo=tiempo
        distancia=self.velocidad*self.tiempo
        self.kilometraje+=distancia
        self.cuenta_kilometros+=distancia
        self.nivel_estanque-=(distancia)/self.rendimiento
        if self.nivel_estanque>=0:
            return 0
        else:
            x=abs(self.nivel_estanque)*self.rendimiento
            return x

    def autonomia(self):
        a=self.nivel_estanque*self.rendimiento
        return a
    
    def llenar_estanque(self,cantidad):
        self.cantidad=cantidad
        if self.cantidad>self.capacidad:
            return (self.capacidad),False
        if self.cantidad<=self.capacidad:
            self.nivel_estanque=self.cantidad
            return (self.cantidad),True

         