#Cajero Automático
usuario = int(input("ingrese numero de usuario: "))
dn = 100000
intento = 3
claveaux = 1803
clave = 0
dnB = 1000000
billete20000 = 20
billete10000 = 40
billete5000 = 40
aux20000 = 0
aux10000 = 0
aux5000 = 0
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
        while monto_retirar > 0:
            if monto_retirar >= 20000:
                monto_retirar = monto_retirar - 20000
                aux20000 = aux20000 + 1
            elif monto_retirar >= 10000:
                monto_retirar = monto_retirar - 10000
                aux10000 = aux10000 + 1
            elif monto_retirar >= 5000:
                monto_retirar = monto_retirar - 5000
                aux5000 = aux5000 + 1
        print("saldo cuenta =", nuevo_saldo)
        print("saldo cajero =", saldo_cajero)
        print("billetes 20000=",aux20000) #"\nbillete de 10000=",aux10000, "\nbillete de 5000=",aux5000 )
        print("billetes 10000=",aux10000)
        print("billetes 5000=",aux5000)
        break      