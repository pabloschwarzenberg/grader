#Cajero Automático
saldo_cuenta = 100000
saldo_cajero = 1000000

intentos = 0
usuario_valido = False

while intentos < 3 and not usuario_valido:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")

    if usuario == "10334151" and clave == "1803":
        usuario_valido = True
    else:
        print("Clave inválida")
        intentos += 1

if intentos == 3:
    print("Tarjeta bloqueada")
else:
    while True:
        monto = int(input("Ingrese el monto a retirar: "))

        if monto > saldo_cuenta:
            print("Monto no permitido")
        else:
            saldo_cuenta -= monto
            saldo_cajero -= monto
            print("Saldo cuenta =", saldo_cuenta)
            print("Saldo cajero =", saldo_cajero)

        continuar = input("¿Desea realizar otro retiro? (S/N): ")

        if continuar.upper() != "S":
            break
      