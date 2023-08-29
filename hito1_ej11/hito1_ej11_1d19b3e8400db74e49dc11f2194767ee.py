#Cajero Automático
      saldo_inicial=1000000
saldo_usuario=100000
intentos=0
billetes_20000=20
billetes_10000=40
billetes_5000=40

while True:
    usuario=input("Ingrese su usuario: ")
    clave=input("Ingrese su clave: ")

    if usuario=="10334151" and clave=="1803":
        print("Ingreso exitoso")
        break
    else:
        intentos=intentos+1
        print("Clave invalida")
    if intentos==3:
        print("Tarjeta bloqueada")
        exit()
while True:
    monto=int(input("Ingrese el monto a retirar: "))
    if monto<=0 or monto>saldo_usuario:
        print("Monto no permitido")
    else:
        if monto>((billetes_20000*20000)+(billetes_10000*10000)+(billetes_5000*5000)):
            print("Nohay suficientes billetes para realizar el retiro")
        else:
            billetes_retirados_20=min(monto//20000,billetes_20000)
            monto=monto-billetes_retirados_20*20000
            billetes_retirados_10=min(monto//10000,billetes_10000)
            monto=monto-billetes_retirados_10*10000
            billetes_retirados_5=min(monto//5000,billetes_5000)
            monto=monto-billetes_retirados_5*5000

            saldo_usuario=saldo_usuario-((billetes_retirados_20*20000)+(billetes_retirados_10*10000)+(billetes_retirados_5*5000))
            saldo_inicial=saldo_inicial-((billetes_retirados_20*20000)+(billetes_retirados_10*10000)+(billetes_retirados_5*5000))
            billetes_20000 -= billetes_retirados_20
            billetes_10000 -= billetes_retirados_10
            billetes_5000 -= billetes_retirados_5
            
            print("Retiro exitoso\n")
            print("Saldo cuenta:", saldo_usuario)
            print("Saldo cajero:", saldo_inicial)
            print("Billetes 20000:", billetes_retirados_20)
            print("Billetes 10000:", billetes_retirados_10)
            print("Billetes 5000:", billetes_retirados_5)
            print()