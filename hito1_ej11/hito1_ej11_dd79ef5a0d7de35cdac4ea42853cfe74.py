tiposbilletes = [20000, 10000, 5000]
usuario_clave_platatotal = [10334151, 1803, 100000]
total_cajero = [20, 40, 40, 1000000]

usuario = int(input("Ingrese su usuario: "))
while not (usuario == usuario_clave_platatotal[0]):
    usuario = int(input("ingrese nuevamente su usuario: "))

clave = int(input("Ingrese su clave: "))
intentos = 1
while clave != usuario_clave_platatotal[1] and intentos < 3:
    intentos = intentos + 1
    clave = int(input("Clave invalida, Reintente: "))

if intentos == 3:
    print("Clave bloqueada")
else:
    montoaRetirar = int(input("Ingrese monto a retirar: "))
    if montoaRetirar >= total_cajero[3] or montoaRetirar >= usuario_clave_platatotal[2]:
        print("Monto no permitido")
    else:
        usuario_clave_platatotal[2] = usuario_clave_platatotal[2] - montoaRetirar
        total_cajero[3] = total_cajero[3] - montoaRetirar
        print("saldo cuenta=", usuario_clave_platatotal[2])
        print("saldo cajero=", total_cajero[3])
        saldo = montoaRetirar
        salidaBilletes = [0, 0, 0]
        while saldo > 0:
            if saldo >= tiposbilletes[0]:
                saldo = saldo - tiposbilletes[0]
                salidaBilletes[0] = salidaBilletes[0] + 1
            if saldo >= tiposbilletes[1]:
                saldo = saldo - tiposbilletes[1]
                salidaBilletes[1] = salidaBilletes[1] + 1
            if saldo >= tiposbilletes[2]:
                saldo = saldo - tiposbilletes[2]
                salidaBilletes[2] = salidaBilletes[2] + 1
        print("billetes", tiposbilletes[0], "=", salidaBilletes[0])
        print("billetes", tiposbilletes[1], "=", salidaBilletes[1])
        print("billetes", tiposbilletes[2], "=", salidaBilletes[2])

