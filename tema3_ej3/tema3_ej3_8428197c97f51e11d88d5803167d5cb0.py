class CuentaCorriente:
    def __init__(self, rut: str, saldo: float):
        self.rut = rut
        self.saldo = saldo

    def girar(self, monto: float) -> bool:
        if monto <= self.saldo:
            self.saldo -= monto
            return True
        else:
            return False
           