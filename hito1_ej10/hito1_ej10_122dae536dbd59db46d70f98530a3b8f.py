#Cajero Automático
 saldo_inicial = 1000000
saldo_usuario = 100000
intentos_fallidos = 0

def pedir_clave():
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")

    if usuario == "10334151" and clave == "1803":
        return True
    else:
        return False

while intentos_fallidos < 3:
    if pedir_clave():
        while True:
            monto_retiro = int(input("Ingrese el monto a retirar: "))

            if monto_retiro <= saldo_usuario:
                saldo_usuario -= monto_retiro
                saldo_inicial -= monto_retiro
                print("Retiro exitoso.")
                print("Nuevo saldo en la cuenta corriente:", saldo_usuario)
                print("Nuevo saldo en el cajero:", saldo_inicial)
                break
            else:
                print("Monto no permitido.")
    else:
        intentos_fallidos += 1
        if intentos_fallidos < 3:
            print("Clave inválida. Intenta nuevamente.")
        else:
            print("Tarjeta bloqueada.")
     