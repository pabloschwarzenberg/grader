class Auto:
    def __init__(self,capacidad_estanque,rendimiento):
        self.kilometraje=0
        self.cuenta_kilometros=0
        self.nivel_estanque=0
        self.capacidad_estanque=capacidad_estanque
        self.rendimiento=rendimiento

    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros=0
 

    def andar(self,velocidad,tiempo):
        km=int(velocidad)/int(tiempo)
        lts=km/int(self.rendimiento)
        self.kilometraje=self.kilometraje+km
        self.cuenta_kilometros=self.cuenta_kilometros+km
        self.nivel_estanque=self.nivel_estanque-lts
        if lts<=self.nivel_estanque:
            return 0
        elif lts>self.nivel_estanque:
            lts_falt=lts-self.nivel_estanque
            km_falt=int(self.rendimiento)*lts_falt
            return km_falt

    def autonomia(self):
        self.kms_posibles=int(self.rendimiento)*int(self.nivel_estanque)
        return self.kms_posibles
    
    def llenar_estanque(self,cant_litros):
        if cant_litros>self.capacidad_estanque-self.nivel_estanque:
            return self.capacidad_estanque,False
        else:
            self.nivel_estanque+=cant_litros
            return self.nivel_estanque,True


         