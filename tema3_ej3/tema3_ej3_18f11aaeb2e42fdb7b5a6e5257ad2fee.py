class CuentaCorriente:
    def __init__(self, rut, saldo):
        self.rut = rut
        self.saldo = saldo

    def girar(self, monto):
        if self.saldo >= monto:
            self.saldo -= monto
            return True
        else:
            return False

if __name__ == "__main__":
    cuenta_1 = CuentaCorriente("12864303-6", 10000)
    print("Saldo inicial:", cuenta_1.saldo)
    
    if cuenta_1.girar(500):
        print("Giro exitoso. Nuevo saldo:", cuenta_1.saldo)
    else:
        print("No se pudo realizar el giro. Saldo insuficiente.")

    if cuenta_1.girar(700):
        print("Giro exitoso. Nuevo saldo:", cuenta_1.saldo)
    else:
        print("No se pudo realizar el giro. Saldo insuficiente.")
