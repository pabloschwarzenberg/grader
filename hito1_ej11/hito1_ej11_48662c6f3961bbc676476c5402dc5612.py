#Cajero Automático
def billetes(m):
    b20 = 0
    b10 = 0
    b5 = 0
    while m != 0:
        if m >= 20000:
            b20 += 1
            m -= 20000
        elif m >= 10000:
            b10 += 1
            m -= 10000
        elif m >= 5000:
            b5 += 1
            m -= 5000
        else:
            return "N"
        
    return b20, b10, b5


cajero = 1000000
cuenta = 100000

billetes20 = 20
billetes10 = 40
billetes5 = 40

usuario = input("Usuario: ")

monto = 1000001
salida = "N"
seguridad = 0
while salida == "N":
    while seguridad != 3:
        clave = input("Clave: ")
        if clave != "1803":
            print("Clave inválida")
            seguridad += 1

            if seguridad == 3:
                print("Tarjeta bloqueada")
                salida = "S"

        else:
            break

    while salida == "N" and seguridad != 3:
        monto = int(input("Monto a retirar: "))
        if monto > cuenta or billetes(monto) == "N":
            print("Monto no permitido")

        else:
            a, b, c = billetes(monto)
            cajero -= monto
            cuenta -= monto

            billetes20 -= a
            billetes10 -= b
            billetes5 -= c

            print("billetes 20000={}".format(a))
            print("billetes 10000={}".format(b))
            print("billetes 5000={}".format(c))
            
            print("Saldo cuenta={}".format(cuenta))
            print("Saldo cajero={}".format(cajero))

            salida = input("¿Salir? S/N: ")