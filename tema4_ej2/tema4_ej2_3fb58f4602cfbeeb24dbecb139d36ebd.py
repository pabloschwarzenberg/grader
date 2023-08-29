class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.kilometraje=0
        self.cuenta_kilometros=0
        self.capacidad_estanque=capacidad_estanque
        self.rendimiento=rendimiento
        self.nivel_estanque=0
    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros=0
        re=self.cuenta_kilometros
        return re
    def andar(self,velocidad,tiempo):
        viaje=velocidad*tiempo
        cap_viaje=self.capacidad_estanque*self.rendimiento
        viaje_logrado=self.nivel_estanque*self.rendimiento
        while self.nivel_estanque!=0:
          self.kilometraje+=1
          if self.cuenta_kilometros%self.rendimiento==0:
            self.nivel_estanque=self.nivel_estanque-1
          self.cuenta_kilometros+=1
          if self.cuenta_kilometros==viaje:
            break
        if self.cuenta_kilometros==viaje:
          if self.nivel_estanque<0:
            falta=abs(viaje-viaje_logrado)
            return falta
          elif self.nivel_estanque>=0:
            return 0,self.nivel_estanque
    
    def autonomia(self):
        pos_viaje=self.nivel_estanque*self.rendimiento
        return pos_viaje
    def llenar_estanque(self,cantidad_de_litros):
        pos=self.nivel_estanque
        pos=pos+cantidad_de_litros
        if pos>self.capacidad_estanque:
          cap=abs(self.capacidad_estanque-self.nivel_estanque)
          return cap,False
        elif pos<=self.capacidad_estanque:  
          self.nivel_estanque=pos
          return self.nivel_estanque, True
        

    
    
    
        

if __name__ == "__main__":
    auto=Auto(100,12)
         