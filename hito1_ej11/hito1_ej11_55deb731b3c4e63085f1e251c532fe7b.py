#Cajero Automático
print("El saldo inicial del cajero es 1.000.000")
print('Introduzca un usuario y una contraseña válida')
count=1
while count <= 3:
    username = int(input('Enter username: '))
    password = int(input('Enter password: '))
    if password == 1803 and username == 10334151:
        print('clave valida')
        x = "N"
        while x == "N":
            if x != "N":
                break
            else:
                SB = 100000
                SAR = int(input('Ingrese su saldo a retirar: '))
                SBF = SB - SAR
                if SAR >= 100000:
                    print("Monto no permitido")
                else:
                    SC = 1000000 - SAR
                    print("saldo cuenta={}".format(SBF))
                    print("saldo cajero={}".format(SC))
            x = input("")
            billetes_20000 = 20
            billetes_10000 = 40
            billetes_5000 = 40
            print("billetes 20000=1")
            print("billetes 10000=1")
            print("billetes 5000=1")
        break

    elif count == 3:
        print("tarjeta bloqueada")
        break
    else:
        print('clave invalida')
        count += 1