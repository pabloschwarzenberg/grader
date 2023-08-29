class Auto:
    def __init__(self,capacidad_estanque,rendimiento):
        self.kilometraje = 0
        self.cuenta_kilometros = 0
        self.capacidad_estanque = capacidad_estanque
        self.nivel_estanque = 0
        self.rendimiento = rendimiento
    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros=0
    def andar(self,v,t):
        recorrido=v*t
        posible=self.nivel_estanque*self.rendimiento
        litrosg=recorrido/self.rendimiento
        if recorrido<=posible:
            self.kilometraje=self.kilometraje+recorrido
            self.cuenta_kilometros=self.cuenta_kilometros+recorrido
            self.nivel_estanque=self.nivel_estanque-litrosg
        else:
            self.cuenta_kilometros=self.cuenta_kilometros+posible
            self.nivel_estanque=0
            self.kilometraje=self.kilometraje+posible
    def autonomia(self):
        a=self.rendimiento*self.nivel_estanque
        return a
    def llenar_estanque(self,l):
        t=()
        if (self.nivel_estanque+l)<=self.capacidad_estanque:
            self.nivel_estanque=self.nivel_estanque+l
            t=(self.nivel_estanque,True)
            
            
        else:
            m=self.capacidad_estanque-self.nivel_estanque
            t=(m,False)
            
        return t