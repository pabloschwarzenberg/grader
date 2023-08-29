saldo_cuenta = 100000
saldo_cajero = 1000000
intentos = 0
usuario = 10334151
clave = 1803

while intentos < 3:
    input_usuario = int(input("Ingrese su número de usuario: "))
    input_clave = int(input("Ingrese su clave: "))

    if input_usuario == usuario and input_clave == clave:
        monto_retiro = int(input("Ingrese el monto a retirar: "))
        if monto_retiro > saldo_cuenta or monto_retiro <= 0:
            print("Monto no permitido")
        else:
            saldo_cuenta -= monto_retiro
            saldo_cajero -= monto_retiro
            print("Saldo cuenta =", saldo_cuenta)
            print("Saldo cajero =", saldo_cajero)
        break
    else:
        intentos += 1
        print("Clave inválida")

if intentos == 3:
    print("Tarjeta bloqueada")
