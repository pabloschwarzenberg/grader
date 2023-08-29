#entradas
veinte_mil = 20
diez_mil = 10
cinco_mil = 40
saldo_cajero = 1000000
saldo_persona = 100000

usuario = int(input("Ingresa tu usuario: "))
clave = int(input("Ingresa tu clave: "))

if clave == 1803:
    monto = int(input("Ingresa el monto a retirar: "))
    if monto > saldo_persona:
        print("monto invalido")
    saldo_persona = saldo_persona - monto
    saldo_cajero = saldo_cajero - monto
    print("saldo cuenta=",saldo_persona)
    print("saldo cajero=",saldo_cajero)
if clave != 1803:
    usuario = int(input("Ingresa tu usuario: "))
    clave = int(input("Ingresa tu clave: "))
    if clave == 1803:
        monto = int(input("Ingresa el monto a retirar: "))
        if monto > saldo_persona:
            print("monto invalido")
        saldo_persona = saldo_persona - monto
        saldo_cajero = saldo_cajero - monto
        print("saldo cuenta=",saldo_persona)
        print("saldo cajero=",saldo_cajero)
if clave != 1803:
    usuario = int(input("Ingresa tu usuario: "))
    clave = int(input("Ingresa tu clave: "))
    if clave == 1803:
        monto = int(input("Ingresa el monto a retirar: "))
        if monto > saldo_persona:
            print("monto invalido")
        saldo_persona = saldo_persona - monto
        saldo_cajero = saldo_cajero - monto
        print("saldo cuenta=",saldo_persona)
        print("saldo cajero=",saldo_cajero)
if clave != 1803:
    print("Clave invalida")
    
      