#Cajero Automático
saldo_inicial = 1000000
saldo_usuario = 100000
intentos = 0
usuario_valido = False

while not usuario_valido:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")
    
    if usuario == "10334151" and clave == "1803":
        usuario_valido = True
        break
    
    intentos += 1
    
    if intentos >= 3:
        print("Tarjeta bloqueada")
        exit()
    else:
        print("Clave inválida")
    
monto_retiro = float(input("Ingrese el monto a retirar: "))

if monto_retiro > saldo_usuario:
    print("Monto no permitido")
else:
    saldo_usuario -= monto_retiro
    saldo_cajero = saldo_inicial - saldo_usuario
    
    print("Saldo cuenta:", saldo_usuario)
    print("Saldo cajero:", saldo_cajero)

