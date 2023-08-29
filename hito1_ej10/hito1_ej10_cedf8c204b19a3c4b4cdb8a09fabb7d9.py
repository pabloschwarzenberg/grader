#Cajero Automático
usuario = int(input("ingrese numero de usuario: "))
dn = 100000
intento = 3
claveaux = 1803
clave = 0
dnB = 1000000
while clave != claveaux:
    intento = intento - 1
    clave =int(input("ingrese numero de clave: "))
    if intento == 0:
        print("tarjeta bloqueada")
        break
    elif clave != claveaux:
        print("clave invalida")

while clave == claveaux:
        monto_retirar = int(input("ingrese monto a retirar: "))
        if monto_retirar > dn:
            print("Monto no permitido")
        elif 0 <=monto_retirar <=dn:
            nuevo_saldo = dn - monto_retirar
            saldo_cajero = dnB - monto_retirar
        print("saldo cuenta =", nuevo_saldo)
        print("saldo cajero =", saldo_cajero)
        break      