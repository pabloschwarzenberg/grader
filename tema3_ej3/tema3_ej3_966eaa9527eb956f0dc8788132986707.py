class Cuenta:

    def __init__(self,rut,saldo):
        self.rut = rut
        self.saldo = saldo


    def girar(self,monto):
        if self.saldo >= monto:
            self.saldo -= monto
            return True
        else:
            return False

    def __repr__(self):
        s = 'Rut: {0} \n' \
            'Saldo: ${1}'.format(self.rut,self.saldo)
        return s