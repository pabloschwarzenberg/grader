class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.kilometraje=0
        self.cuenta_kilometros=0
        self.capacidad_estanque=capacidad_estanque
        self.nivel_estanque=0
        self.rendimiento=rendimiento
    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros=0
    def andar(self,velocidad,tiempo):
        distancia=velocidad*tiempo
        self.kilometraje=self.kilometraje+distancia
        self.cuenta_kilometros=self.cuenta_kilometros+distancia
        litros_gastados=distancia*(self.rendimiento)**(-1)
        if self.nivel_estanque>=litros_gastados:
            self.nivel_estanque=self.nivel_estanque-litros_gastados
            return 0
        else:
          resta=litros_gastados-self.nivel_estanque
          kilometros=int(self.rendimiento*resta)
          return kilometros
    def autonomia(self):
        calculo=self.nivel_estanque*self.rendimiento
        return calculo
    def llenar_estanque(self,litros):
        completo=self.nivel_estanque+litros
        if completo>self.capacidad_estanque:
            return (self.capacidad_estanque,False)
        else:
            self.nivel_estanque=self.nivel_estanque+litros
            return (self.nivel_estanque,True)


          
        

if __name__ == "__main__":
    auto=Auto(100,12)
         