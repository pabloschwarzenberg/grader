class Auto:
    def init(self, m, e, c):
        self.marca= m #el valor lo tiene que definir el usuario.
        self.motor= False #valor inicial es falso.
        self.ruedas= [2.3, 1.9, 1.0, 2.7] #el valor inicial es esa lista.
        self.estanque= e
        self.color= c

    def __str__(self):
        return (f"La marca del auto es {self.marca}.")

    def llave(self):
        if self.motor== True:
            self.motor= False
        else:
            self.motor= True

    def inflar_ruedas(self, limite_inflado):
        for ruedita in range(len(self.ruedas)): #aquí no se puede poner solo "in" porque eso lee el dato, pero no lo modifica.
            #en cambio range(len()) lee la posición y deja reemplazarla.
            #ruedita es la posición.
            if self.ruedas[ruedita] < límite_inflado: #es [] por ser una posición.
                self.ruedas[ruedita]= 3.0 #cambia el valor de self.ruedas a 3.0 si es menor al límite de inflado.

    def llenar_tanque(self, agregar):
        z= self.estanque + agregar
        if z > 100:
            print("No se puede llenar más el estanque.")
        else:
            print("Su tanque ahora tiene " ,z)




carro= Auto("audi", 50, "rojo") #para la marca del auto, el relleno y el color.
carro2= Auto("jeep", 79, "naranja")
print(carro.marca)
print(carro)
print(carro2)