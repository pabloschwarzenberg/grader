#Cajero Automático
class CajeroAutomatico:
    def __init__(self):
        self.saldo_cajero = {
            20000: 20,
            10000: 40,
            5000: 40
        }
        self.saldo_inicial = sum(billetes * cantidad for billetes, cantidad in self.saldo_cajero.items())
        self.saldo_actual = self.saldo_inicial

    def iniciar_sesion(self):
        while True:
            cuenta = input("Ingrese el número de cuenta: ")
            clave = input("Ingrese la clave: ")
            if cuenta == "10334151" and clave == "1803":
                print("Inicio de sesión exitoso.")
                return True
            else:
                print("Número de cuenta o clave incorrectos. Intente nuevamente.")

    def retirar_dinero(self):
        monto = int(input("Ingrese el monto a retirar: "))
        if monto > self.saldo_actual:
            print("Saldo insuficiente.")
            return

        billetes_entregados = {
            20000: 0,
            10000: 0,
            5000: 0
        }

        # Distribuir los billetes según el monto solicitado
        for billete, cantidad in self.saldo_cajero.items():
            while monto >= billete and cantidad > 0:
                monto -= billete
                cantidad -= 1
                billetes_entregados[billete] += 1

        # Actualizar el saldo del cajero y mostrar los resultados
        self.saldo_cajero = {
            billete: cantidad
            for billete, cantidad in self.saldo_cajero.items()
        }
        self.saldo_actual -= sum(billete * cantidad for billete, cantidad in billetes_entregados.items())

        print("Billetes entregados:")
        for billete, cantidad in billetes_entregados.items():
            if cantidad > 0:
                print("{billete} = {cantidad}")

        print("Saldo cuenta =", self.saldo_actual)
        print("Saldo cajero =", self.saldo_actual)

    def ejecutar_cajero(self):
        if not self.iniciar_sesion():
            print("Tarjeta bloqueada.")
            return

        while True:
            opcion = input("¿Desea realizar un retiro? (S/N): ")
             if opcion.upper() == "N":
                print("Gracias por utilizar el cajero automático.")
                break
             elif opcion.upper() == "S":
                self.retirar_dinero()
             else:
                print("Opción inválida. Intente nuevamente.")


cajero = CajeroAutomatico()
cajero.ejecutar_cajero()
      