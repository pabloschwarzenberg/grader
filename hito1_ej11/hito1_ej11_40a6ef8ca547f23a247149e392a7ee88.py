#Cajero Automático
dinero_cajero = 1000000
billetes_20 = 20
billetes_10 = 40
billetes_5 = 40
numero_usuario = int(input("ingrese su numero de usuario: "))
clave = int(input("ingrese su clave: "))
contador = 0
while numero_usuario != 10334151 or clave != 1803:
    contador += 1
    print("clave invalida")
    if contador == 3:
        print("tarjeta bloqueada")
        break
    numero_usuario = int(input("Ingrese su numero de usuario nuevamente: "))
    clave = int(input("ingrese su clave nuevamente: "))

if contador < 3:
    saldo_cuenta = 100000
    while True:
        retiro = int(input("ingrese el total a retirar: "))
        if retiro == "N":
            break
        elif int(retiro) > dinero_cajero or int(retiro) <= 0 or int(retiro) > saldo_cuenta:
            print("monto invalido")
        else:
            dinero_cajero = dinero_cajero - int(retiro)
            saldo_cuenta -= int(retiro)
            billetes_20_retiro = int(retiro)//20000
            billetes_10_retiro = (int(retiro) - billetes_20_retiro*20000)//10000
            billetes_5_retiro = (int(retiro) - billetes_20_retiro*20000 - billetes_10_retiro*10000)//5000
            billetes_20 -= billetes_20_retiro
            billetes_10 -= billetes_10_retiro
            billetes_5  -= billetes_5_retiro                     
            print("billetes20000=" + str(billetes_20_retiro))
            print("billetes10000=" + str(billetes_10_retiro))
            print("billetes5000=" + str(billetes_5_retiro))
            print("saldo cuenta =" + str(saldo_cuenta))
            print("saldo cajero =" + str(dinero_cajero))
            break
            
          