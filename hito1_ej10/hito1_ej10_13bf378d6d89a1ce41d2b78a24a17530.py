#Cajero Automático
saldo_cuenta = 100000
saldo_cajero = 1000000
intentos = 0

usuario_valido = 10334151
clave_valida = 1803

while intentos < 3:
    usuario = int(input("Ingrese su usuario: "))
    clave = int(input("Ingrese su clave: "))

    if usuario == usuario_valido and clave == clave_valida:
        monto_retiro = int(input("Ingrese el monto a retirar: "))

        if monto_retiro > saldo_cuenta:
            print("Monto no permitido")
        else:
            saldo_cuenta -= monto_retiro
            saldo_cajero -= monto_retiro
            print("Saldo cuenta =", saldo_cuenta)
            print("Saldo cajero =", saldo_cajero)
        break
    else:
        print("Clave inválida")
        intentos += 1

if intentos == 3:
    print("Tarjeta bloqueada")
      