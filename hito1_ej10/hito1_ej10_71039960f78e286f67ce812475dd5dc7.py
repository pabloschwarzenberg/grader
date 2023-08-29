#Cajero Automático
saldoCajero = 1000000
saldoCliente = 100000

user = input("Ingrese Usuario: ")
clave = input("Ingrese su Clave: ")

if user == '10334151' and clave == '1803':
    monto = int(input("Ingrese el monto a retirar: "))
    saldoCliente = saldoCliente - monto
    saldoCajero = saldoCajero - monto
    print('saldo cuenta=',saldoCliente)
    print('saldo cajero=',saldoCajero)