class Auto:
    def __init__(self,capacidad_estanque,rendimiento):
        self.kilometraje=0
        self.cuenta_kilometros=0
        self.capacidad_estanque=capacidad_estanque
        self.nivel_estanque=0           #litros de combustible
        self.rendimiento=rendimiento  #km x litro, km que puede recorrer x litro
        
    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros=0            
        
    def andar(self,velocidad,tiempo):               #kilometraje, cuenta_km, litros actuales
        recorrido_total=velocidad*tiempo    #100 (km/h)* 3 (horas)= 300 km total
        litros_necesarios=recorrido_total/self.rendimiento  #300km/3(km/litro) = 100litros
        self.kilometraje=self.kilometraje+recorrido_total               #km=200, =>km=200+300 =km=500   
        self.cuenta_kilometros=self.cuenta_kilometros+recorrido_total    
        if(litros_necesarios<=self.nivel_estanque):                         #500 litros,  100 litros,                          
            self.nivel_estanque=self.nivel_estanque-litros_necesarios       #500= > 500-100=> 400 litros
            return(0)                                                       #llego correctamente
        else:                                   
            litros_faltantes=litros_necesarios-self.nivel_estanque          #50 litros, 100 litros, litros faltaron=50
            recorrido_faltante=litros_faltantes*self.rendimiento            #litros necesitamos-litros del auto, 
            return(recorrido_faltante)
            
    def autonomia(self):
        km_posibles=self.rendimiento*self.nivel_estanque                    #3(km/litro)* 100litros= 300km
        return(km_posibles)
    
    def llenar_estanque(self,litros):
        max_cargar=self.capacidad_estanque-self.nivel_estanque              # 100 litros- 40 litros=> 60 litros
        if (max_cargar>=litros):                                            # 30 litros, 60 litros, 
            self.nivel_estanque=self.nivel_estanque+litros                  # 30 litros= 40 litros => 70 litros
            return((self.nivel_estanque,True))                              #   se recarga
        else:
            return((max_cargar,False))                                         #60 litros, False 
            
            
def viaje(auto,km,tiempo):
    viaje_total=km*tiempo               #recorrido total
    contador=0                          #cont=0
    while(viaje_total>0):               #ciclos         viaje_total=80km, viaje_total=60km            
        auto1.llenar_estanque(100)                      
        viaje_total=viaje_total-(auto.autonomia())          #recorrido_total-recorrido_avanzado, 100 litros, 40km, 100 km, 20km->80 km
        auto.andar(km,tiempo)                               #80km -> 20km, 60km ->20km
        contador=contador+1                                 #  cont=1, cont=2, cont=3           
    return(contador)
            
if __name__ == "__main__":
   
    auto1=Auto(100,12)                      #12km por litro
                                            #100 litros maximo    
    x=viaje(auto1,120,32)                   
    print("Se necesita recargar el vehiculo "+str(x)+" veces.")