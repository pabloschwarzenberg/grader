class Cajero:
            def __init__(self):
                self.continuar =[True]
                self.montocajero = 1000000
                self.montousuario = 100000
                self.contraseña()
                self.retiro()


            def contraseña(self):
                contador = 1
                while contador <= 3:
                    x = int(input("Ingrese su usuario:"))
                    y = int(input("Ingrese su clave:"))
                    if x == 10334151 and y == 1803:
                        print("Contraseña correcta")
                        break
                    else:
                        print("Clave invalida")
                        if contador == 3:
                            print ("tarjeta bloqueada")
                            self.continuar = False
                        contador = contador + 1
            def retiro (self):
                retirar = int(input("Ingrese monto a retirar: "))
                if retirar > self.montocajero:
                    print ("monto no disponible")
                if retirar > self.montousuario:
                    print ("monto no disponible")
                else:
                    self.montousuario = self.montousuario - retirar
                    print ("saldo cuenta=",self.montousuario)
                    self. montocajero = self.montocajero - retirar
                    print ("saldo cajero=",self.montocajero)

app = Cajero()