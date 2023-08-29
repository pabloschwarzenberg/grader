class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.kilometraje=0
        self.cuenta_kilometros=0
        self.nivel_estanque=0
        self.capacidad_estanque=capacidad_estanque
        self.rendimiento = rendimiento
    def llenar_estanque(self,litros):
        if((self.nivel_estanque+litros)<self.capacidad_estanque):            
            self.nivel_estanque=self.nivel_estanque+litros
            return (self.nivel_estanque,True)
        else:
            return (self.capacidad_estanque,False)
    def autonomia(self):
        return(self.nivel_estanque*12)
    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros=0
    def andar(self,velocidad,tiempo):
        KmxLitro=velocidad/tiempo
        Litro=KmxLitro/12
        if (Litro<=self.capacidad_estanque):        
            self.kilometraje=self.kilometraje+KmxLitro
            self.cuenta_kilometros=self.cuenta_kilometros+KmxLitro
            self.nivel_estanque=self.nivel_estanque-Litro
            return 0
        else:
            return ( (Litro-self.capacidad_estanque)*12 )
         