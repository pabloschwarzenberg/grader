#Cajero Automático
saldo_cuenta = 100000
saldo_cajero = 1000000
intentos = 0

def validar_clave(usuario, clave):
    if usuario == "10334151" and clave == "1803":
        return True
    return False

def realizar_retiro(monto):
    global saldo_cuenta, saldo_cajero
    if monto > saldo_cuenta or monto > saldo_cajero:
        print("Monto no permitido")
    else:
        saldo_cuenta -= monto
        saldo_cajero -= monto
        print("Retiro exitoso")
        print("Saldo cuenta =", saldo_cuenta)
        print("Saldo cajero =", saldo_cajero)

# Iniciar el programa
print("Bienvenido al cajero automático")
usuario = "10334151"
clave = "1803"

while intentos < 3:
    if validar_clave(usuario, clave):
        break
    else:
        print("Clave inválida")
        intentos += 1
        if intentos == 3:
            print("Tarjeta bloqueada")
            exit()

retiro1 = 45000
realizar_retiro(retiro1)

retiro2 = 30000
realizar_retiro(retiro2)

print("Gracias por utilizar el cajero automático")
