class CajeroAutomatico:
    def __init__(self):
        self.billetes_disponibles = {20000: 20,10000: 40,5000: 40}

    def imprimir_saldos(self):
        print("Saldo disponible:")
        for denominacion, cantidad in self.billetes_disponibles.items():
            print("Billetes", denominacion, " = ", cantidad)

    def retirar_dinero(self, monto):
        print("Retirando", monto, "pesos...")
        billetes_entregados = {}
        for denominacion, cantidad in self.billetes_disponibles.items():
            if monto >= denominacion:
                cantidad_billetes = min(cantidad, monto // denominacion)
                if cantidad_billetes > 0:
                    billetes_entregados[denominacion] = cantidad_billetes
                    monto -= denominacion * cantidad_billetes
        if monto == 0:
            print("Billetes entregados:")
            for denominacion, cantidad in billetes_entregados.items():
                print("Billetes", denominacion, "=", cantidad)
            self.actualizar_saldo(billetes_entregados)
        else:
            print("No se puede retirar el monto solicitado. Por favor, intenta con otro monto.")

    def actualizar_saldo(self, billetes_entregados):
        for denominacion, cantidad in billetes_entregados.items():
            self.billetes_disponibles[denominacion] -= cantidad


