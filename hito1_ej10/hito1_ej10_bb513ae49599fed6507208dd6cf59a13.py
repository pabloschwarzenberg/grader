#Cajero Automático
usuario = int(input("Favor ingrese el usuario: "))

clave = int(input("Favor ingrese su clave: "))

intentos = 1
saldo_cajero = 1000000
saldo_usuario = 100000
usuariocorrecto = 10334151
clavecorrecta = 1803

while clave != clavecorrecta:
    intentos += 1
    if clave == clavecorrecta:
        print("clave incorrecta")
        break

    if intentos > 3:
        break
    print("clave invalida")

    clave = int(input("Ingrese su clave nuevamente: "))

if intentos > 3:
    print("tarjeta bloqueada")

if usuario == usuariocorrecto:
    if clave == clavecorrecta:
        monto = int(input("¿Cuanto monto desea retirar?: "))
        if monto > saldo_usuario and monto > saldo_cajero:
            print("monto no perimitido")
        else:
            saldo_usuario -= monto
            saldo_cajero -= monto

            print("saldo cuenta=" + str(saldo_usuario))
            print("saldo cajero=" + str(saldo_cajero))