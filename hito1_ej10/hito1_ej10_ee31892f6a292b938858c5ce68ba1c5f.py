#Cajero Automático
def Monto(monto,Cajero=1000000,Usuario=100000):
    if monto > Cajero:
        return "Monto no permitido"
    else:
        Usuario = Usuario - monto
        Cajero = Cajero - monto
        print("saldo cuenta=",Usuario)
        print("saldo cajero=",Cajero)
        return [Usuario,Cajero]

x = 0
y = 0
intentos = 0
while y == 0:
    if x == 0:
        print("Usuario")
        input()
        print("clave")
        clave = input()
        if clave == "1803":
            x = 1
        elif intentos == 2:
            print("Tarjeta bloqueada")
            break
        else:
            intentos = intentos + 1
    elif x == 1:
        print("Ingrese monto a retirar")
        z = input()
        di = "qwertyuiopñlkjhgfdsazxcvbm,.-{}+´¿QWERTYUIOPÑLKJHGFDSAZXCVBM"
        if z in di:
            break
        elif z == "N":
            x = 1
        else:
            Monto(float(z))     