#Cajero Automático
cuenta = 100000
saldo_inicial = 1000000
intentos_fallidos = 0
b_20000 = 20
b_10000 = 40
b_5000 = 40

while True:
    usuario = (input("Ingrese su número de usuario: "))
    clave = (input("Ingrese su clave: "))
    
    if usuario == '10334151' and clave == '1803':
        break
    else:
        intentos_fallidos += 1
        print("Clave inválida")
        
        if intentos_fallidos == 3:
            print("Tarjeta bloqueada")
  
while True:
    monto = int(input("Ingrese el monto a retirar: "))
    
    if monto <= 0:
        print("Monto no valido")
    elif monto > cuenta or monto > saldo_inicial:
                print("No hay saldo suficiente")
    else:
        cuenta -= monto
        saldo_inicial -= monto
        print(['saldo cuenta=' + str(cuenta), 'saldo cajero=' + str(saldo_inicial)])

    if monto > b_20000 * 20000 + b_10000 * 10000 + b_5000 * 5000:
            print("No hay suficientes billetes")
    else:
        billetes_20000_retirados = min(monto // 20000, b_20000)
        monto -= billetes_20000_retirados * 20000
        billetes_10000_retirados = min(monto // 10000, b_10000)
        monto -= billetes_10000_retirados * 10000
        billetes_5000_retirados = min(monto // 5000, b_5000)
        monto -= billetes_5000_retirados * 5000
        b_20000 -= billetes_20000_retirados
        b_10000 -= billetes_10000_retirados
        b_5000 -= billetes_5000_retirados
        print("Billetes 20000 =", billetes_20000_retirados)
        print("Billetes 10000 =", billetes_10000_retirados)
        print("Billetes 5000 =", billetes_5000_retirados)
        opcion = str('Ingrese una letra distinta a n para salir: ')
            
        if opcion != "n":
            break
    