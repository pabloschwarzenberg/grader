#Cajero Automático
class Cajero:
    def __init__(self, saldoCajero):
        self.saldoCajero = saldoCajero
    
    def validarSaldo(self):
        self.saldoCajero > montoRetirar
        return True
    
    def montoCajero(self):
        self.saldoCajero -= montoRetirar
        return saldoCajero

class Cuenta:
    def __init__(self, usuario, clave, montoInicial):
        self.usuario = usuario
        self.clave = clave
        self.montoInicial = montoInicial
    #@classmethod
    def validarSaldo(self):
        self.montoInicial < montoRetirar
        return True
        
    def validarClave(self, clavecomparar):
        print(clavecomparar)
        if self.clave == clavecomparar:
            return True
        else:
            return False

cuenta1 = Cuenta("10334151", "1803", "100000")
saldoCajero = 1000000

usuario = int(input('Usuario: '))
intentos = 3
while 0 < intentos <= 3:
    clave = input('Clave: ')
    if cuenta1.validarClave(clave):
        break
    else:
        print("Clave invalida")
        intentos -= 1
        print("Le quedan",intentos ,"intentos.")
        continue
if intentos == 0:
    print('Tarjeta bloqueda')
    exit()

while True:
    montoRetirar = int(input('Monto a retirar: '))
    if Cuenta.validarSaldo:
        if Cajero.validarSaldo:
            Cajero.montoCajero
            #montoFinal = Cuenta.validarSaldo - montoRetirar
            montoFinal = Cuenta.montoInicial - montoRetirar
            print("Saldo cuenta =", montoFinal)
            print("Saldo cajero =", Cajero.saldoCajero)
            break
            exit()
        else:
            print('Saldo insuficiente')
            continue
    else:
        print('Monto superior')
        continue
     