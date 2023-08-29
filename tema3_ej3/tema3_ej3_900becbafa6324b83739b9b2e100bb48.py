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
rut =int(input("ingrese su rut:"))
saldo =int(input("ingrese su saldo actual:"))
monto=int(input("ingrese el monto en que desea girar:"))
cuenta = CuentaCorriente("rut", saldo)

if cuenta.girar(monto):
    print("Giro exitoso")
else:
    print("No se puede realizar el giro")