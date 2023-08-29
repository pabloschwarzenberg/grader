saldo_cuenta = 1000000
billetes_20000 = 20
billetes_10000 = 40
billetes_5000 = 40

def retirar_dinero(clave, monto):
    global saldo_cuenta, billetes_20000, billetes_10000, billetes_5000
    
    if clave != "1803":
        print("Clave inválida")
        return
    
    if monto % 5000 != 0:
        print("Monto no permitido")
        return
    
    if monto > saldo_cuenta:
        print("Saldo insuficiente")
        return
    
    billetes_20000_entregados = min(monto // 20000, billetes_20000)
    monto -= billetes_20000_entregados * 20000
    billetes_20000 -= billetes_20000_entregados
    
    billetes_10000_entregados = min(monto // 10000, billetes_10000)
    monto -= billetes_10000_entregados * 10000
    billetes_10000 -= billetes_10000_entregados
    
    billetes_5000_entregados = min(monto // 5000, billetes_5000)
    monto -= billetes_5000_entregados * 5000
    billetes_5000 -= billetes_5000_entregados
    
    saldo_cuenta -= (billetes_20000_entregados * 20000) + (billetes_10000_entregados * 10000) + (billetes_5000_entregados * 5000)
    
    print("Billetes entregados:")
    print("billetes 20000 =", billetes_20000_entregados)
    print("billetes 10000 =", billetes_10000_entregados)
    print("billetes 5000 =", billetes_5000_entregados)
    print("Saldo cuenta =", saldo_cuenta)
    print("Saldo cajero =",(billetes_20000 * 20000) + (billetes_10000 * 10000) + (billetes_5000 * 5000))

intentos = 0
while intentos < 3:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")

    if usuario == "10334151" and clave == "1803":
        monto = int(input("Ingrese el monto a retirar: "))
        retirar_dinero(clave, monto)
        break

    print("Usuario o clave incorrectos. Intente nuevamente.")
    intentos += 1

if intentos == 3:
    print("Tarjeta bloqueada")
  