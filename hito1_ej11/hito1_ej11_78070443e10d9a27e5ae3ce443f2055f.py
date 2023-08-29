saldo_inicial = 1000000
saldo_usuario = 100000
intentos = 0

usuario_correcto = 10334151
clave_correcta = 1803

billetes_20000 = 20
billetes_10000 = 40
billetes_5000 = 40

usuario = int(input("Ingrese su usuario: "))
clave = int(input("Ingrese su clave: "))

if usuario == usuario_correcto and clave == clave_correcta:
    print("Acceso permitido")
else:
    print("Usuario o clave incorrectos")
    exit()

while True:
    monto = int(input("Ingrese el monto a retirar: "))

    if monto <= 0 or monto > saldo_usuario:
        print("Monto no permitido")
        continue

    if monto > saldo_inicial:
        print("Saldo insuficiente en el cajero")
        continue

    
    if monto % 5000 != 0 or monto > (billetes_20000 * 20000 + billetes_10000 * 10000 + billetes_5000 * 5000):
        print("El cajero no dispone de los billetes necesarios para el monto solicitado")
        continue

    
    billetes_20000_retiro = min(monto // 20000, billetes_20000)
    monto -= billetes_20000_retiro * 20000

    billetes_10000_retiro = min(monto // 10000, billetes_10000)
    monto -= billetes_10000_retiro * 10000

    billetes_5000_retiro = min(monto // 5000, billetes_5000)
    monto -= billetes_5000_retiro * 5000

    
    saldo_usuario -= (billetes_20000_retiro * 20000 + billetes_10000_retiro * 10000 + billetes_5000_retiro * 5000)
    saldo_inicial -= (billetes_20000_retiro * 20000 + billetes_10000_retiro * 10000 + billetes_5000_retiro * 5000)
    billetes_20000 -= billetes_20000_retiro
    billetes_10000 -= billetes_10000_retiro
    billetes_5000 -= billetes_5000_retiro

    
    print("saldo cuenta =", saldo_usuario)
    print("saldo cajero =", saldo_inicial)
    print("billetes 20000 =", billetes_20000_retiro)
    print("billetes 10000 =", billetes_10000_retiro)
    print("billetes 5000 =", billetes_5000_retiro)

    break

      