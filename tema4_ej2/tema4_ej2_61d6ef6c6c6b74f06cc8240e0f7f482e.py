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

        if litros_necesarios <= self.nivel_estanque:
            self.kilometraje += distancia
            self.cuenta_kilometros += distancia
            self.nivel_estanque -= litros_necesarios
            return 0
        else:
            kilometros_faltantes = (self.nivel_estanque * self.rendimiento) - distancia
            self.kilometraje += (self.nivel_estanque * self.rendimiento)
            self.cuenta_kilometros += (self.nivel_estanque * self.rendimiento)
            self.nivel_estanque = 0
            return kilometros_faltantes

    def autonomia(self):
        return self.nivel_estanque * self.rendimiento

    def llenar_estanque(self, cantidad_litros):
        litros_totales = self.nivel_estanque + cantidad_litros

        if litros_totales <= self.capacidad_estanque:
            self.nivel_estanque = litros_totales
            return (self.nivel_estanque, True)
        else:
            litros_maximos = self.capacidad_estanque - self.nivel_estanque
            return (litros_maximos, False)

        
if __name__ == "__main__":
    auto=Auto(100,12)
    viaje_distancia = 500  
    viaje_velocidad = 80  
    viaje_tiempo = viaje_distancia / viaje_velocidad 

    veces_detenerse = 0
    kilometros_recorridos = 0

    while kilometros_recorridos < viaje_distancia:
        resultado = auto.andar(viaje_velocidad, viaje_tiempo)
        if resultado == 0:
            kilometros_recorridos += viaje_distancia
        else:
            kilometros_recorridos += viaje_distancia - resultado
            veces_detenerse += 1

    print("Número de veces que tendrás que detenerte a cargar combustible:", veces_detenerse)