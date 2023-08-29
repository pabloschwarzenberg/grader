# completa el código de la función
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

rut = input("Ingrese su RUT: ")
saldo = int(input("Ingrese su saldo inicial: "))

mi_cuenta = CuentaCorriente(rut, saldo)

monto = int(input("Ingrese el monto a girar: "))
if mi_cuenta.girar(monto):
    print("Giro exitoso. Nuevo saldo:", mi_cuenta.saldo)
else:
    print("Fondos insuficientes.")