#Cajero Automático
saldo_inicial = 1000000
saldo_usuario = 100000
intentos = 0

usuario_valido = 10334151
clave_valida = 1803

billetes_20000 = 20
billetes_10000 = 40
billetes_5000 = 40

usuario = int(input("Ingrese su número de usuario: "))
clave = int(input("Ingrese su clave: "))

if usuario == usuario_valido and clave == clave_valida:
    print("Acceso permitido")
    
    monto = int(input("Ingrese el monto a retirar: "))

    if monto > saldo_usuario:
        print("Monto no permitido")
    else:
        saldo_usuario -= monto
        saldo_inicial -= monto
        print("Retiro exitoso")
        
        round_usuario = round(saldo_usuario)
        round_inicial = round(saldo_inicial)
        
        print("saldo cuenta =", round_usuario)
        print("saldo cajero =", round_inicial)

        billetes_entregados = {
            20000: 0,
            10000: 0,
            5000: 0
        }
        
        
        while monto >= 20000 and billetes_20000 > 0:
            billetes_entregados[20000] += 1
            monto -= 20000
            billetes_20000 -= 1
        
        while monto >= 10000 and billetes_10000 > 0:
            billetes_entregados[10000] += 1
            monto -= 10000
            billetes_10000 -= 1
        
        while monto >= 5000 and billetes_5000 > 0:
            billetes_entregados[5000] += 1
            monto -= 5000
            billetes_5000 -= 1
        
        
        for billete, cantidad in billetes_entregados.items():
            if cantidad > 0:
                print("billetes", billete, "=", cantidad)
else:
    print("Clave inválida")
    intentos += 1

    if intentos == 3:
        print("Tarjeta bloqueada")      