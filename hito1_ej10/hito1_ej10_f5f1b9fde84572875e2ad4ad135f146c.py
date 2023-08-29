#Cajero Automático
intentos = 0
clave_correcta = 1803
usuario_correcto = 10334151
saldo_cajero = 1000000
saldo_cuenta = 100000

while intentos < 3:
    usuario_ingresado = int(input("Ingrese su usuario: "))
    clave_ingresada = int(input("Ingrese su clave: "))

    if clave_ingresada == clave_correcta and usuario_ingresado == usuario_correcto:
        monto = int(input("Ingrese un monto a retirar: "))

        if monto < 0:
            print("Monto no permitido")
        else:
            saldo_cajero -= monto
            saldo_cuenta -= monto
            print("Saldo cuenta =", saldo_cuenta)
            print("Saldo cajero =", saldo_cajero)
        break

    else:
        print("Credenciales inválidas")
        intentos += 1

if intentos >= 3:
    print("Tarjeta bloqueada")