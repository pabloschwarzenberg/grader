#Crea la clase Auto, con los siguientes atributos:

#kilometraje: Cuando se crea el auto, parte en 0. A medida que se usa, el kilometraje va aumentando.

#cuenta_kilometros: Cuando se crea el auto, parte en 0.
#Este atributo debe llevar la cuenta de los kilómetros recorridos desde la última vez que se reinició el cuenta kilómetros.

#capacidad_estanque: Indica la capacidad máxima de combustible que puede almacenar el auto (se debe recibir como parámetro en el constructor).

#nivel_estanque: Indica la cantidad de litros de combustible que tiene actualmente el estanque. Es menor o igual a la capacidad máxima.
#Al crear el auto debe partir en 0.


#rendimiento: Número que indica la cantidad de kilómetros por litro que rinde el auto (se debe recibir como parámetro en el constructor).


#Define en la Clase Auto los siguientes métodos:

#reiniciar_cuentakilometros: Reinicia a 0 el valor del cuenta kilómetro.

#andar: Recibe una velocidad y un tiempo de viaje. Con esto debe actualizar los litros actuales, el kilometraje, y el cuenta kilómetros.
#Si se pudo terminar con éxito el viaje debe retornar 0. En caso de quedarse sin bencina, debe retornar la cantidad de kilómetros que faltó por recorrer.

#autonomia: Debe retornar cuántos kilómetros puede recorrer el auto con los litros de combustible que posee actualmente.

#llenar_estanque: Recibe como parámetro la cantidad de litros y actualiza los litros actuales. Si es que se le intenta echar más combustible de lo que soporta el auto,
#debe retornar una tupla con dos valores: la máxima cantidad de combustible que se le puede echar al estanque y False. Si es que logró llenar el estanque con éxito,
#la tupla debe indicar los litros con los que quedó el auto y True.

#Usando la clase auto, crea un programa que te indique cuántas veces tendrás que detenerte a cargar combustible en un determinado viaje.
#Considera un auto con un estanque de 100 litros y 12 km/l de rendimiento.

class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.capacidad_estanque = capacidad_estanque
        self.kilometraje = 0
        self.rendimiento = rendimiento
        self.cuenta_kilometros = 0
        self.nivel_estanque = 0

    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros = 0 # se reinicia cuenta kilometros

    def andar(self,velocidad,tiempo):
        self.kilometraje = self.kilometraje + (velocidad*tiempo*60*60) #se modifica cantidad de kilometros recorridos
        self.cuenta_kilometros = self.cuenta_kilometros + (velocidad*tiempo)  # se modifica cuenta_kilometros
        self.nivel_estanque = self.capacidad_estanque - (velocidad*tiempo)/self.rendimiento #litros que quedan
        if self.nivel_estanque >= 0:
            return 0
        else:
            return(-(self.nivel_estanque*self.rendimiento)) # los km que faltaron
    def autonomia(self):
        return((self.nivel_estanque)*self.rendimiento) #los km que puede recorrer con los litros que tiene
    def llenar_estanque(self,litros):
        if self.nivel_estanque + litros <= self.capacidad_estanque:
            self.nivel_estanque = self.nivel_estanque + litros
            return(self.nivel_estanque+ litros,True)
        else:
            return(self.capacidad_estanque-self.nivel_estanque,False)

    def __str__(self):
        return str(self.capacidad_estanque) + "-" + str(self.kilometraje) + "-" + str(self.rendimiento) + "-" + str(self.cuenta_kilometros) + "-" + str(self.nivel_estanque)


if __name__ == "__main__":
    auto=Auto(60,12)
    b = auto.andar(120,1)
    print(b)
    print(auto)
