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
        se_puede_recorrer=self.rendimiento*self.nivel_estanque
        por_recorrer=velocidad*tiempo
        litros_que_se_ocuparon=por_recorrer/self.rendimiento
        if por_recorrer>se_puede_recorrer:
            kms_que_faltaron=por_recorrer-se_puede_recorrer
            self.kilometraje+=se_puede_recorrer
            self.cuenta_kilometros+=se_puede_recorrer
            self.nivel_estanque=0
            return kms_que_faltaron
        else:
            self.kilometraje+=por_recorrer
            self.cuenta_kilometros+=por_recorrer
            self.nivel_estanque-=litros_que_se_ocuparon
            return 0
    def autonomia(self):
        kms=self.rendimiento*self.nivel_estanque
        return kms
    def llenar_estanque(self,litros):
        self.nivel_estanque=litros
        if self.capacidad_estanque<self.nivel_estanque:
            return self.capacidad_estanque,False
        else: 
            return self.nivel_estanque,True
if __name__ == "__main__":
      auto=Auto(100,12)