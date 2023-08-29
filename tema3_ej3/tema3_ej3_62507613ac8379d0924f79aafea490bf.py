class Cuenta:
    def __init__(self, rut, saldo ):
            self.rut=rut
            self.saldo=saldo
    def __init__(self, girar):
        if self.girar>=girar:
            self.girar=self.saldo-girar
            return True
        else:
            False