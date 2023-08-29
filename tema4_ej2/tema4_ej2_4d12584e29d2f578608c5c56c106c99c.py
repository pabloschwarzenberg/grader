class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.kilometraje = 0
        self.cuenta_kilometros = 0
        self.capacidad_estanque = capacidad_estanque
        self.nivel_estanque = 0
        self.rendimiento = rendimiento
        
    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros = 0
        
    def andar(self, velocidad, tiempo):
        distancia = velocidad * tiempo
        litros_necesarios = distancia / self.rendimiento
        if litros_necesarios > self.nivel_estanque:
            distancia_faltante = (litros_necesarios - self.nivel_estanque) * self.rendimiento
            self.kilometraje += distancia - distancia_faltante
            self.cuenta_kilometros += distancia
            self.nivel_estanque = 0
            return distancia_faltante
        else:
            self.kilometraje += distancia
            self.cuenta_kilometros += distancia
            self.nivel_estanque -= litros_necesarios
            return 0
        
    def autonomia(self):
        return self.nivel_estanque * self.rendimiento
        
    def llenar_estanque(self, litros):
        if self.nivel_estanque + litros > self.capacidad_estanque:
            max_litros = self.capacidad_estanque - self.nivel_estanque
            self.nivel_estanque = self.capacidad_estanque
            return (max_litros, False)
        else:
            self.nivel_estanque += litros
            return (self.nivel_estanque, True)
        

auto = Auto(100, 12) # Auto con estanque de 100 litros y rendimiento de 12 km/l

# Calculamos la cantidad de paradas necesarias para un viaje de 1000 km a una velocidad constante de 80 km/h
distancia_total = 1000
velocidad = 80
tiempo = distancia_total / velocidad
paradas_necesarias = 0
while distancia_total > 0:
    autonomia = auto.autonomia()
    if distancia_total <= autonomia:
        auto.andar(velocidad, tiempo)
        distancia_total = 0
    else:
        auto.andar(velocidad, autonomia / velocidad)
        distancia_total -= autonomia
        paradas_necesarias += 1
    if auto.nivel_estanque == 0:
        max_litros, exito = auto.llenar_estanque(100)
        if not exito:
            print("No se puede continuar el viaje, el estanque está lleno y aún faltan {} km por recorrer".format(distancia_total))
            break
        else:
            print("Se llenó el estanque con {} litros".format(max_litros))

print("Se necesitan {} paradas para completar el viaje".format(paradas_necesarias))