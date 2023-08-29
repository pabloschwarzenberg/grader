#Cajero Automático
saldo_inicial_cajero = 1000000
saldo_inicial_usuario = 100000
intentos_fallidos = 0

def validar_clave(usuario, clave):
    if usuario == '10334151' and clave == '1803':
        return True
    else:
        return False

def retirar_dinero(monto, saldo_usuario, saldo_cajero):
    if monto > saldo_usuario:
        print("Monto no permitido. Saldo insuficiente.")
    elif monto > saldo_cajero:
        print("Monto no permitido. Cajero sin suficiente dinero.")
    else:
        saldo_usuario -= monto
        saldo_cajero -= monto
        print("Retiro exitoso.")
        print("Saldo cuenta=", saldo_usuario)
        print("Saldo cajero=", saldo_cajero)
        return saldo_usuario, saldo_cajero

usuario = input("Ingrese su usuario: ")
clave = input("Ingrese su clave: ")

if validar_clave(usuario, clave):
    saldo_usuario = saldo_inicial_usuario
    saldo_cajero = saldo_inicial_cajero
    print("Bienvenido(a) al cajero automático.")
    
    while True:
        monto = float(input("Ingrese el monto a retirar: "))
        saldo_usuario, saldo_cajero = retirar_dinero(monto, saldo_usuario, saldo_cajero)
        
        opcion = input("¿Desea realizar otro retiro? (S/N): ")
        if opcion.upper() != 'S':
            break
else:
    print("Clave inválida. Intento fallido.")
    intentos_fallidos += 1
    
    if intentos_fallidos >= 3:
        print("Tarjeta bloqueada. Ha alcanzado el máximo de intentos permitidos.")

print("Gracias por utilizar el cajero automático. ¡Hasta luego!")