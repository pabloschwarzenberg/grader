#Clase Auto:

class Auto:

    #Para setear los atributos al momento de crear la instancia de la
    #clase, definimos el constructor
    def __init__(self, capacidad_estanque, rendimiento):
        #Si bien son 5 atributos, como hay atributos que sabemos
        #a priori que cuando se crean valdrC!n 0, podemos no pedir esos
        #valores y fijarlos directamente en 0
        self.capacidad_estanque = capacidad_estanque
        self.rendimiento = rendimiento
        self.kilometraje = 0
        self.cuenta_kilometros = 0
        self.nivel_estanque = 0


    #Las siguientes 2 funciones, como toda la informacion
    #estC! contenida dentro del mismo auto, no reciben ningC:n
    #parC!metro (Este tipo de mC)todos, se puede utilizar
    #para actualizar el estado del objeto a valores que
    #no dependen de algo exterior, o para entregar
    #informacion del objeto al programa principal)
    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros = 0

    def autonomia(self):
        return self.rendimiento*self.nivel_estanque

    #los siguientes mC)todos, como buscan actualizar el estado
    #del auto dadas ciertas condiciones exteriores al objeto
    #reciben parC!metros(ya sea litros que echarC!, o velocidad y
    #tiempo que anduvo el auto)
    def llenar_estanque(self, litros):
        #Aqui hay que tener presente, que los litros actuales no
        #pueden sobrepasar la capacidad mC!xima.
        if self.nivel_estanque + litros > self.capacidad_estanque:
            print("No se puede echar tal cantidad de bencina, lo máximo que "+
                  "le puede echar es",self.capacidad_estanque - self.nivel_estanque)
            return self.capacidad_estanque - self.nivel_estanque,False
        else:
            self.nivel_estanque += litros
            print("Bencina echada con éxito, el auto ahora tiene "+
                  "{0} litros".format(self.nivel_estanque))
            return self.nivel_estanque,True

    def andar(self, velocidad, tiempo):
        #Para ver si me quedo en pana o no, primero fijo lo que
        #en teorC-a alcanzarC-a a andar sin quedarme en pana
        kilometros_por_recorrer = velocidad*tiempo
        #Luego, si la autonomia (Si! podemos utilizar un mC)todo
        #de la misma clase, dentro de otro metodo) es menor a
        #los kilometros recorridos en la teorC-a, quiere decir que
        #nos quedamos en pana.

        if self.autonomia() < kilometros_por_recorrer:
            #Como nos quedamos en pana, actualizamos los kilometros
            #andados al valor real, y dejamos los litros actuales
            #en 0, que eso es, por definicion, quedarse en pana
            kilometros_andados = self.autonomia()
            print("El auto se quedo en pana, alcanzó a andar "+
                  "{} kilometros".format(kilometros_andados))
        else:
            kilometros_andados=kilometros_por_recorrer

        #ahora que tengo los kilometros recorridos para cualquiera de los
        #2 casos, actualizo el estado de mi auto
        self.nivel_estanque -= kilometros_andados/self.rendimiento
        self.kilometraje += kilometros_andados
        self.cuenta_kilometros += kilometros_andados
        return kilometros_por_recorrer-kilometros_andados

if __name__ == "__main__":
    #Para ver que está todo bien, creamos un auto que puede almacenar 100 litros
    #y rinde 12 kilometros por litro
    auto = Auto(100,12)

    #Le echamos 60 litros de bencina
    auto.llenar_estanque(60)

    #Tratamos de echarle otros 60 litros, para corroborar que no puede pasar
    #los 100 litros, y que nos diga correctamente cuanto es lo mC!ximo que
    #podemos echar
    auto.llenar_estanque(60)

    #Vemos que está correcta la autonomia
    print("Autonomia:",auto.autonomia())

    #Hacemos andar el auto durante 1 hora, a 48 kilometros por hora
    #y vemos si efectivamente actualiza el estado del auto
    auto.andar(120,1)
    print(auto.kilometraje, auto.cuenta_kilometros, auto.nivel_estanque)

    #reiniciamos el cuenta kilómetros
    auto.reiniciar_cuentakilometros()
    print("Cuenta kilometros:",auto.cuenta_kilometros)

    #Andamos otra vez, pero esta vez hasta quedarnos en pana, y vemos
    #Como queda el auto.
    auto.andar(120,12)
    print(auto.kilometraje, auto.cuenta_kilometros, auto.nivel_estanque)

