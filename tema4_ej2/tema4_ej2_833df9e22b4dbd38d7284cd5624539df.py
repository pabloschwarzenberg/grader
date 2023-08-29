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
        a=velocidad*tiempo
        b=self.nivel_estanque*self.rendimiento
        c=a/self.rendimiento
        if a<=b:
            self.cuenta_kilometros=self.cuenta_kilometros+a
            self.kilometraje=self.kilometraje+a
            self.nivel_estanque=self.nivel_estanque-c
            return(0)
        else:
            self.cuenta_kilometros=self.cuenta_kilometros+b
            self.kilometraje=self.kilometraje+b
            self.nivel_estanque=0
            resta=a-b
            return(resta)

    def autonomia(self):
        km=self.rendimiento*self.nivel_estanque
        return(km)

    def llenar_estanque(self,litros):
        if self.nivel_estanque+litros<=self.capacidad_estanque:
            self.nivel_estanque=self.nivel_estanque+litros
            return(self.nivel_estanque,True)
        else:
            total=self.capacidad_estanque-self.nivel_estanque
            return(total,False)
        