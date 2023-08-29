#Cajero Automático
saldoCajero = 1000000
bi20mil = 20
bi10mil = 40
bi5mil = 40
usuarioValido = 10334151
claveValida = 1803
saldoCuenta = 100000
usuario = int(input("Ingrese usuario: "))
while usuario != usuarioValido:
    usuario = int(input("ingrese usuario nuevamente: "))

clave = int(input("Ingrese clave: "))    
intentos = 0
while clave != claveValida:
    if intentos == 3:
        print("tarjeta bloqueada")
        break
    clave = int(input("clave invalida: "))    
if intentos != 3: #continuo el programa si la clave no esta bloqueada
    montoRetirado = int(input("Ingrese monto"))
    if montoRetirado>saldoCajero or montoRetirado>saldoCuenta:
        print("monto no permitido")
    else:
        saldoCajero = saldoCajero - montoRetirado
        saldoCuenta = saldoCuenta - montoRetirado
        cuentabi20mil = 0
        cuentabi10mil = 0
        cuentabi5mil = 0
        while (montoRetirado>0):
            if montoRetirado >= 20000:
                cuentabi20mil = cuentabi20mil + 1
                bi20mil = bi20mil - 1
                montoRetirado = montoRetirado - 20000
            if montoRetirado >= 10000:
                cuentabi10mil = cuentabi10mil + 1
                bi10mil = bi10mil - 1
                montoRetirado = montoRetirado - 10000 #montoRetirado- 15000
            if montoRetirado >= 5000:
                cuentabi5mil = cuentabi5mil + 1
                bi5mil = bi5mil - 1
                montoRetirado = montoRetirado - 5000 #montoRetirado- 10000              
        print("saldo cuenta=", saldoCuenta)
        print("saldo cajero=", saldoCajero)
        print("billetes 20000=", cuentabi20mil)
        print("billetes 10000=", cuentabi10mil)
        print("billetes 5000=", cuentabi5mil)
