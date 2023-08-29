class CajeroAutomatico:
    def __init__(self):
        self.billetes = {
            20000: 20,
            10000: 40,
            5000: 40
        }

    def imprimir_saldos(self):
        saldo_cuenta = self.calcular_saldo_cuenta()
        saldo_cajero = self.calcular_saldo_cajero()
        print("Saldo cuenta =", saldo_cuenta)
        print("Saldo cajero =", saldo_cajero)

    def realizar_giro(self, monto):
        saldo_cuenta = self.calcular_saldo_cuenta()
        if monto <= saldo_cuenta:
            billetes_entregados = {denominacion: 0 for denominacion in self.billetes}

            for denominacion in sorted(self.billetes, reverse=True):
                cantidad_disponible = self.billetes[denominacion]
                cantidad_entregada = min(monto // denominacion, cantidad_disponible)
                monto -= cantidad_entregada * denominacion
                billetes_entregados[denominacion] = cantidad_entregada

            if monto == 0:
                for denominacion, cantidad_entregada in billetes_entregados.items():
                    self.billetes[denominacion] -= cantidad_entregada

                print("Retiro exitoso.")
                print("Cantidad de billetes entregados:")
                for denominacion, cantidad_entregada in billetes_entregados.items():
                    print(f"Billetes de {denominacion}:", cantidad_entregada)
            else:
                print("No es posible realizar el retiro.")
        else:
            print("No hay saldo suficiente en la cuenta.")

    def calcular_saldo_cuenta(self):
        saldo = 0
        for denominacion, cantidad in self.billetes.items():
            saldo += denominacion * cantidad
        return saldo

    def calcular_saldo_cajero(self):
        saldo = 0
        for denominacion, cantidad in self.billetes.items():
            saldo += denominacion * cantidad
        return saldo


# Ejemplo de uso
cajero = CajeroAutomatico()
cajero.imprimir_saldos()

monto_retiro = 15000
cajero.realizar_giro(monto_retiro)

cajero.imprimir_saldos()
