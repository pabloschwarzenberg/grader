def operacion(monto,Caja=1000000,persona=100000):
    if monto > Caja:
        return "Monto no permitido"
    else:
        persona = persona - monto
        Caja = Caja - monto
        print("saldo cuenta=",persona)
        print("saldo cajero=",Caja)
        return [persona,Caja]

c = 0
b = 0
intentos = 0
while b == 0:
    if c == 0:
        print("Usuario")
        input()
        print("clave")
        passw = input()
        if passw == "1803":
            c = 1
        elif intentos == 2:
            print("Tarjeta bloqueada")
            break
        else:
            intentos += 1
    elif c == 1:
        print("Ingrese monto a retirar")
        p = input()
        di = "qwertyuiopñlkjhgfdsazxcvbm,.-{}+´¿QWERTYUIOPÑLKJHGFDSAZXCVBM"
        if p in di:
            break
        elif p == "N":
            c = 1
        else:
            operacion(float(p))