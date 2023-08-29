class Cuenta:
    rut = []
    saldo = []

    def __init__(self,rut,saldo):
        self.rut = rut
        self.saldo = saldo



datos = Cuenta("20471930-6",350)
print(datos.saldo)
def girar(self):
    if datos.saldo < 100000:
        print(f"se puede transgerir: {datos.saldo}")
    else:
        print("no se puede transferir")