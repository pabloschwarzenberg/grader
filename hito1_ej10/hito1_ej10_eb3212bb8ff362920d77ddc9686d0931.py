saldo_inicial = 1000000
saldo_cajero = 1000000
intentos_fallidos = 0

# Función para validar la clave
def validar_clave(clave):
    return clave == "1803"

# Pedir usuario y clave
usuario = input("Usuario: ")
clave = input("Clave: ")

# Verificar el usuario y la clave
if usuario == "10334151" and validar_clave(clave):
    saldo_cuenta = 100000
    print("Bienvenido,", usuario)

    monto = int(input("Ingrese el monto a retirar: "))

    # Verificar el monto a retirar
    if monto <= 0:
        print("Monto no permitido")
    else:
        # Realizar el retiro
        if monto <= saldo_cuenta:
            saldo_cuenta -= monto
            saldo_cajero -= monto
            print("Retiro exitoso")
            print("saldo cuenta=" + str(saldo_cuenta))
            print("saldo cajero=" + str(saldo_cajero))
        else:
            print("Saldo insuficiente")
else:
    print("Tarjeta bloqueada")