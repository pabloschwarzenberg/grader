#Crea una clase que represente la Cuenta Corriente del Cliente de un Banco. Debe tener un atributo rut y uno saldo, los cuales deben ser recibidos como parámetro por el constructor para ser inicializados. Debe tener un método llamado girar, el cual debe retornar True si el saldo de la cuenta permite hacer el giro, y False en caso contrario.
#Si el giro se puede realizar, debe restar el monto a girar del saldo de la cuenta.

class Cuenta:
    def __init__(self,rut,saldo):
        self.rut=rut
        self.saldo=saldo

    def girar(self,monto):
        if monto<=self.saldo:
            self.saldo-=monto
            return True
        else:
            return False
    
if __name__ == "__main__":
    cuenta=Cuenta("12345678-9",100000)
    print(cuenta.girar(50000))
    print(cuenta.saldo)
    print(cuenta.girar(80000))
    print(cuenta.saldo)