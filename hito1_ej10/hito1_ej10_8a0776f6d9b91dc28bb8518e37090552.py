#Cajero Automático
usuario = int(input("Usuario : "))
clave = int(input("Clave : "))
saldoInicial = 1000000
bloq = 0

while usuario != 10334151 and clave != 1803:
    bloq = bloq + 1
    print('clave invalida')
    if bloq == 3:
        print('tarjeta bloqueada')

if usuario == 10334151 and clave == 1803:
    saldoCuenta = 100000
    montoRetiro = int(input("monto a retirar : "))
    if montoRetiro > saldoCuenta:
        print('monto no permitido')
    if montoRetiro < saldoCuenta:
        montoRetirado = saldoCuenta - montoRetiro
        saldoFinal = saldoInicial - montoRetiro
        print('saldo cuenta=',montoRetirado)
        print('saldo cajero=',saldoFinal)      