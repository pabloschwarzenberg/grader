import os

class Cajero:
 
    def __init__(self):
        self.continuar = True
        self.monto = 100000
        self.menu()
        
    def contraseña(self):
        contador = 1
        while contador <= 3:
            x = int(input("ingrese su contraseña:" ))
            if x == 1803:
                print("Contraseña Correcta")
                break
            else:
                print(f"Contraseña Incorrecta, le quedan {3 - contador} intentos")
                if contador == 3:
                    print("Tarjeta Bloqueada.")
                    self.continuar = False #Corregido?
                    break  #Cortaste el flujo antes de cambiar el estado de continuar
                    #self.continuar = False
                contador+=1
 
    def menu(self):
        #so.system("cls") #CORREGIR A de "SO" A "OS"
        os.system("cls")
        self.contraseña()
        if self.continuar:
            opcion = "0"  #Opcion valida para operar
        else:
            opcion = "4" # Opcion invalida y cierra programa
            print("Programa finalizado")
        while opcion != "4":
            os.system("cls")
            print(""" Bienvenido al cajero automatico
            ******Menú******
            1- Depositar
            2- Retirar
            3- Ver saldo
            4- Salir """)
            opcion = input("Su opción es: ")
            if self.continuar:
                if opcion == "1" :
                    self.depositar()
                elif opcion == "2" :
                    self.retiro()
                elif opcion == "3":
                    self.ver()
                elif opcion == "4":
                    print("Programa finalizado")
                else:
                    print("NO existe esa opción")
            
        
    def depositar(self):
	    dep = int(input("Ingrese su monto a depositar:"))
	    print("Usted a depositado",dep)
	    print(f"Su nuevo saldo es {self.monto + dep}")
	    self.monto+=dep
 
    def retiro(self):
        retirar=int(input("¿Cuánto desea retirar? : "))
        print("Su monto actual es", self.monto)
        if self.monto >= retirar :
            print(f"Usted a retirado: {retirar} , su nuevo monto es {self.monto - retirar}")
            self.monto-=retirar
        else:
            print("Imposible realizar el retiro, su monto es menor")
 
    def ver(self):
        print("Su saldo es: " , self.monto)

app = Cajero()