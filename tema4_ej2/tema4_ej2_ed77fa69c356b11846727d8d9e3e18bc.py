class Auto:
    
    def __init__(self, capacidad_estanque, rendimiento):     
        self.kilometraje = 0
        self.cuenta_kilometros = 0
        self.capacidad_estanque = capacidad_estanque
        self.nivel_estanque = 0
        self.rendimiento = rendimiento
        self.km_totales = capacidad_estanque*rendimiento

    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros = 0


    def andar(self,velocidad,tiempo):
        distancia = velocidad * tiempo
        self.km_vacio = self.nivel_estanque * self.rendimiento
        if distancia > self.km_vacio:
            distancia = distancia - self.km_vacio
            self.nivel_estanque = 0
            return distancia

        else:
            self.km_vacio = self.km_vacio - distancia
            self.nivel_estanque = self.km_vacio/self.rendimiento
            self.kilometraje = self.kilometraje + distancia
            self.cuenta_kilometros = self.cuenta_kilometros + distancia
            return 0
        


        
    def autonomia(self):
        self.autonomia = self.nivel_estanque*self.rendimiento
        return self.autonomia

    def llenar_estanque(self,litros_agregados):
        litros = 0
        tupla = []
        for n in range(litros_agregados + 1):
            litros = litros + 1
            if litros + self.nivel_estanque > self.capacidad_estanque:
                tupla.append(self.capacidad_estanque)
                tupla.append(False)
                return tupla


        self.nivel_estanque = self.nivel_estanque + litros_agregados
        tupla.append(self.nivel_estanque)
        tupla.append(True)
        return tupla
    
    

if __name__ == "__main__":
    auto=Auto(100,12)
    velocidad = int(input("Ingrese la velocidad: "))
    tiempo = int(input("Ingrese el tiempo: "))        
    distancia = velocidad * tiempo
    numero_cargas = 0
    while distancia > 0:
        auto.reiniciar_cuentakilometros()
        if auto.nivel_estanque > 0:
            auto.andar(velocidad,tiempo)
            distancia = distancia - auto.cuenta_kilometros
            print("Distancia restante: ",distancia)

        
        else:
            km_cargados = int(input("No te queda bencina. Cuanto deseas cargar? "))
            if auto.llenar_estanque(km_cargados)[1] == True:
                auto.nivel_estanque = auto.llenar_estanque(km_cargados)[0]
                numero_cargas = numero_cargas + 1
                print("Tu numero de cargas total es: ",numero_cargas)
                continue

            else:
                print("Carga no valida")

  
