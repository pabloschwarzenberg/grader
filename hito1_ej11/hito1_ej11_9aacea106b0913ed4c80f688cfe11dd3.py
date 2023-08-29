#Cajero Automático
class CajeroAutomatico:
    def __init__(self):
        self.billetes = {
            20000: 20,
            10000: 40,
            5000: 40
        }

    def imprimir_saldos(self):
        print("Saldo actual:")
        for denominacion, cantidad in self.billetes.items():
            print(f"Billetes {denominacion} = {cantidad}")

    def retirar_dinero(self, monto):
        print(f"Retirando {monto} pesos...")

        billetes_entregados = {}
        saldo_disponible = sum(denominacion * cantidad for denominacion, cantidad in self.billetes.items())

        if monto > saldo_disponible:
            print("No hay suficiente saldo para realizar el retiro.")
            return

        for denominacion, cantidad in sorted(self.billetes.items(), reverse=True):
            if monto >= denominacion:
                cantidad_entregada = min(monto // denominacion, cantidad)
                monto -= denominacion * cantidad_entregada
                billetes_entregados[denominacion] = cantidad_entregada

        if monto == 0:
            print("Retiro exitoso. Billetes entregados:")
            for denominacion, cantidad in billetes_entregados.items():
                print(f"Billetes {denominacion} = {cantidad}")
            self.actualizar_saldos(billetes_entregados)
        else:
            print("No se puede realizar el retiro con los billetes disponibles.")

    def actualizar_saldos(self, billetes_entregados):
        for denominacion, cantidad in billetes_entregados.items():
            self.billetes[denominacion] -= cantidad

cajero = CajeroAutomatico()
cajero.imprimir_saldos()

monto_a_retirar = 45000
cajero.retirar_dinero(monto_a_retirar)

cajero.imprimir_saldos()
