class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        # Inicializar los atributos de la clase
        self.kilometraje = 0 # Parte en 0
        self.cuenta_kilometros = 0 # Parte en 0
        self.capacidad_estanque = capacidad_estanque # Se recibe como parámetro
        self.nivel_estanque = 0 # Parte en 0
        self.rendimiento = rendimiento # Se recibe como parámetro

    def reiniciar_cuentakilometros(self):
        # Reiniciar el valor del cuenta kilómetros a 0
        self.cuenta_kilometros = 0

    def andar(self, velocidad, tiempo):
        # Calcular la distancia que se quiere recorrer con la velocidad y el tiempo dados
        distancia = velocidad * tiempo
        # Calcular el consumo de combustible que implica la distancia
        consumo = distancia / self.rendimiento
        # Validar que el nivel de estanque sea suficiente para el consumo
        if consumo <= self.nivel_estanque:
            # Actualizar los atributos del auto según el consumo y la distancia
            self.nivel_estanque -= consumo # Restar el consumo al nivel de estanque
            self.kilometraje += distancia # Sumar la distancia al kilometraje
            self.cuenta_kilometros += distancia # Sumar la distancia al cuenta kilómetros
            return 0 # Retornar 0 para indicar que se completó el viaje
        else:
            # Calcular la distancia que se pudo recorrer con el nivel de estanque disponible
            distancia_recorrida = self.nivel_estanque * self.rendimiento
            # Calcular la distancia que faltó por recorrer
            distancia_faltante = distancia - distancia_recorrida
            # Actualizar los atributos del auto según la distancia recorrida
            self.nivel_estanque = 0 # Dejar el nivel de estanque en 0
            self.kilometraje += distancia_recorrida # Sumar la distancia recorrida al kilometraje
            self.cuenta_kilometros += distancia_recorrida # Sumar la distancia recorrida al cuenta kilómetros
            return distancia_faltante # Retornar la distancia faltante para indicar que no se completó el viaje

    def autonomia(self):
        # Calcular y retornar los kilómetros que puede recorrer el auto con el nivel de estanque actual
        return self.nivel_estanque * self.rendimiento

    def llenar_estanque(self, litros):
        # Validar que los litros que se quieren agregar no superen la capacidad máxima del estanque
        if litros <= self.capacidad_estanque - self.nivel_estanque:
            # Actualizar el nivel de estanque con los litros agregados
            self.nivel_estanque += litros
            # Retornar una tupla con el nivel de estanque actual y True para indicar que se llenó con éxito
            return (self.nivel_estanque, True)
        else:
            # Calcular la máxima cantidad de litros que se pueden agregar al estanque sin sobrepasar la capacidad máxima
            max_litros = self.capacidad_estanque - self.nivel_estanque
            # Retornar una tupla con los litros máximos y False para indicar que no se pudo llenar con éxito
            return (max_litros, False)

if __name__ == "__main__":
    # Crear un objeto de la clase Auto con los parámetros dados (100 litros y 12 km/l)
    auto = Auto(100, 12)
    # Pedir al usuario que ingrese la velocidad y el tiempo del viaje (en km/h y h respectivamente)
    velocidad = float(input("Ingrese la velocidad del viaje (km/h): "))
    tiempo = float(input("Ingrese el tiempo del viaje (h): "))
    # Calcular la distancia total del viaje con la velocidad y el tiempo dados
    distancia_total = velocidad * tiempo
    print("La distancia total del viaje es", distancia_total, "km")
    # Crear una variable para contar las veces que se detuvo a cargar combustible
    detenciones = 0 
    # Mientras no se haya completado el viaje, repetir el siguiente proceso
    while distancia_total > 0:
        # Intentar andar con el auto usando la velocidad y el tiempo dados
        distancia_faltante = auto.andar(velocidad, tiempo)
        # Si se completó el viaje, salir del ciclo
        if distancia_faltante == 0:
            break
        # Si no se completó el viaje, actualizar la distancia total que falta por recorrer
        distancia_total = distancia_faltante
        # Aumentar el contador de detenciones en uno
        detenciones += 1
        # Llenar el estanque del auto con la capacidad máxima
        auto.llenar_estanque(auto.capacidad_estanque)
    # Imprimir el número de detenciones que se hicieron para cargar combustible
    print("Se detuvo", detenciones, "veces para cargar combustible")

         