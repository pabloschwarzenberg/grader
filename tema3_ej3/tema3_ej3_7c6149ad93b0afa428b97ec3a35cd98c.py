class Cuenta:
    
    def __init__(self, r, saldo):
        self.r=r
        self.saldo=saldo

    def girar(self,m):
    
        if self.saldo >= m:
            self.saldo= self.saldo-m
            return True
        if self.saldo<m:
            return False