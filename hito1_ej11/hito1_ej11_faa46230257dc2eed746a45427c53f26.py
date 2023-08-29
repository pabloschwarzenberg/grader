#Cajero Automático
saldo = 1000000
bi20mil = 20
bi10mil = 40
bi5mil = 10

usuario = 10334151
clave = 1803
saldoCuenta = 100000

ingreso = int(input("Ingrese el numero de usuario: "))
while ingreso != usuario:
    ingreso = int(input("Ingrese usuario nuevamente: "))

contra = int(input("Ingrese la clave del usuario: "))
intentos = 0
while contra != clave:
    intentos += 1
    contra = int(input("Clave invalida: "))
    if intentos == 3:
        print("Tarjeta bloqueada")
        break
if intentos != 3:
    retiro = int(input("Ingrese monto a retirar: "))
    if retiro > saldo or retiro >= saldoCuenta:
        print("Monto no permitido")
    else:
        saldo = saldo - retiro
        saldoCuenta = saldoCuenta - retiro
        cuentaBi20mil = 0
        cuentaBi10mil = 0
        cuentaBi5mil = 0
        
        while (retiro > 0):
            if retiro >= 20000:
                cuentaBi20mil = cuentaBi20mil + 1
                bi20mil = bi20mil - 1
                retiro = retiro - 20000

            if retiro >= 10000:
                cuentaBi10mil = cuentaBi10mil + 1
                bi10mil = bi10mil - 1
                retiro = retiro - 10000

            if retiro >= 5000:
                cuentaBi5mil = cuentaBi5mil + 1
                bi5mil = bi5mil - 1
                retiro = retiro - 5000

        print("saldo cuenta=",saldoCuenta)
        print("saldo cajero=",saldo)
        print("billetes 20000=",cuentaBi20mil)
        print("billetes 10000=",cuentaBi10mil)
        print("billetes 5000=",cuentaBi5mil)
    
     