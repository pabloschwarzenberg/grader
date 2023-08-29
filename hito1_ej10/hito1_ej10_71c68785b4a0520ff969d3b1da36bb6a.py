#Cajero Automático
platacajero = 1000000 
platausuario = 100000
mal = 0

def valclave(clave):
    return clave == "1803"

def retirar_dinero(monto):
    global platacajero, platausuario
    if monto <= platausuario and monto <= platacajero:
        platacajero -= monto
        platausuario -= monto
        print("Retiro exitoso.")
        print(" saldo  cuenta=", platausuario)
        print(" saldo  cajero=", platacajero)
    else:
        print("Monto no permitido.")

usuario = input("Ingrese el usuario: ")
clave = input("Ingrese la clave: ")

if usuario == "10334151" and valclave(clave):
    while True:
        monto = float(input("Ingrese el monto a retirar: "))
        if monto <= 0:
            print("Monto no permitido.")
            continue
        retirar_dinero(monto)
        break
else:
    print("Clave inválida.")
    mal += 1

if mal >= 3:
    print("Tarjeta bloqueada.")
     