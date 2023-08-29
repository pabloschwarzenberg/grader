class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.capacidad_estanque=int(capacidad_estanque) 
        self.rendimiento=int(rendimiento)  
        self.kilometraje=0 
        self.cuenta_kilometros=0
        self.nivel_estanque=0  
      
    def reiniciar_cuentakilometros(self): 
      self.cuenta_kilometros=0   
      
    def andar(self,velocidad,tiempo):  
      dist_deseada=velocidad*tiempo  
      dist_disponible=self.nivel_estanque*self.rendimiento  
      vencina_gastada=(dist_deseada)/self.rendimiento 
      self.nivel_estanque=self.nivel_estanque-vencina_gastada
      if dist_deseada<=dist_disponible: 
        return 0 
      else: 
        quedo=dist_deseada-dist_disponible 
        return quedo  
        
    def autonomia(self): 
      cant=(self.nivel_estanque)*(self.rendimiento) 
      return cant 
      
    def llenar_estanque(self,litros): 
      if litros>(self.capacidad_estanque-self.nivel_estanque):  
        b=self.capacidad_estanque-self.nivel_estanque
        tuplaa=(b,False)  
        return tuplaa
      elif litros<(self.capacidad_estanque-self.nivel_estanque): 
        c=self.nivel_estanque+litros 
        tuplaaa=(c,True)   
        return tuplaaa
      
      

if __name__ == "__main__":
    auto=Auto(100,12) 
    print(str(auto.autonomia()))
         