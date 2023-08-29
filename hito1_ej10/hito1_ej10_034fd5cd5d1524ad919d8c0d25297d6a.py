saldo_cuenta = 100000
saldo_cajero = 1000000
intentos = 0

while True:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")
    
    if usuario == "10334151" and clave == "1803":
        break
    
    intentos += 1
    
    if intentos == 3:
        print("Tarjeta bloqueada.")
        exit()
    else:
        print("Clave inválida.")
        
while True:
    monto = int(input("Ingrese el monto a retirar: "))
    
    if monto > saldo_cuenta or monto <= 0:
        print("Monto no permitido.")
    else:
        saldo_cuenta -= monto
        saldo_cajero -= monto
        print("Saldo cuenta =", saldo_cuenta)
        print("Saldo cajero =", saldo_cajero)
        break