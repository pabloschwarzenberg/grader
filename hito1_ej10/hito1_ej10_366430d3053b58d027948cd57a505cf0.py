#Cajero Automático
# Entrada
# Saldo del cajero
saldo_cajero = 1000000

# Ingreso del usuario
user = int(input("Ingrese usuario: "))
saldo_usuario = 100000
# Validacion de la clave
clave1 = 1803
clave = 0
i = 0
intentos = 0
# Proceso
while i < 3 and clave != clave1:
    clave = int(input("Ingrese clave: "))
    if clave != clave1:
        print("Clave invalida")
        intentos += 1
        if intentos == 3:
            print("*** Tarjeta bloqueada ***")
    # Monto a retirar de la cuenta
    else:
        if clave == clave1:
            retiro = int(input("Monto a retirar: "))
            if retiro > saldo_usuario:
                print("*** Monto Invalido ***")
                retiro = int(input("Monto a retirar: "))
                if retiro <= saldo_usuario:
                    saldo_usuario = saldo_usuario - retiro
                    saldo_cajero = saldo_cajero - retiro
            elif retiro <= saldo_usuario:
                saldo_usuario = saldo_usuario - retiro
                saldo_cajero = saldo_cajero - retiro

    i += 1
# Salida
print("Saldo cuenta", "=", saldo_usuario)
print("Saldo cajero", "=", saldo_cajero)