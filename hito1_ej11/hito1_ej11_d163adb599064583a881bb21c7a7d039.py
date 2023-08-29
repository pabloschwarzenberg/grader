class CajeroAutomatico:
    def __init__(self):
        self.saldo_20000 = 20
        self.saldo_10000 = 40
        self.saldo_5000 = 40

    def mostrar_saldos(self):
        print("Saldo de billetes:")
        print("Billetes de 20.000: ", self.saldo_20000)
        print("Billetes de 10.000: ", self.saldo_10000)
        print("Billetes de 5.000: ", self.saldo_5000)

    def retirar_dinero(self, monto):
        total_retirado = 0
        billetes_20000 = 0
        billetes_10000 = 0
        billetes_5000 = 0

        while monto > 0:
            if monto >= 20000 and self.saldo_20000 > 0:
                monto -= 20000
                self.saldo_20000 -= 1
                billetes_20000 += 1
                total_retirado += 20000
            elif monto >= 10000 and self.saldo_10000 > 0:
                monto -= 10000
                self.saldo_10000 -= 1
                billetes_10000 += 1
                total_retirado += 10000
            elif monto >= 5000 and self.saldo_5000 > 0:
                monto -= 5000
                self.saldo_5000 -= 1
                billetes_5000 += 1
                total_retirado += 5000
            else:
                break

        if total_retirado == 0:
            print("No hay suficiente saldo para realizar el retiro.")
        else:
            print("Se ha retirado un total de", total_retirado, "pesos:")
            print("Billetes de 20.000:", billetes_20000)
            print("Billetes de 10.000:", billetes_10000)
            print("Billetes de 5.000:", billetes_5000)

# Crear una instancia del cajero automático
cajero = CajeroAutomatico()

# Mostrar los saldos iniciales
cajero.mostrar_saldos()

# Solicitar al usuario el monto a retirar
monto_retiro = int(input("Ingrese el monto a retirar: "))

# Realizar el retiro
cajero.retirar_dinero(monto_retiro)

# Mostrar los saldos actualizados
cajero.mostrar_saldos()
