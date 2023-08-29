class CuentaCorriente:
    def __init__(self, rut, saldo):
        self.rut = rut
        self.saldo = saldo

    def girar(self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
            return True
        else:
            return False

if __name__ == "__main__":
    rut = input("Ingrese el RUT del cliente: ")
    saldo_inicial = float(input("Ingrese el saldo inicial: "))
    cuenta = CuentaCorriente(rut, saldo_inicial)

    monto_giro = float(input("Ingrese el monto a girar: "))
    if cuenta.girar(monto_giro):
        print("Giro exitoso. Saldo restante:", cuenta.saldo)
    else:
        print("Saldo insuficiente para realizar el giro.")
