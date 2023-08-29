#Cajero Automático
intento=0

while intento < 3:
    usuario = input("ingrese su usuario: ")
    intento= intento + 1
    cuenta = 100000
    cajero = 1000000

    if usuario == "10334151":
        clave = input("ingrese su clave: ")
        if clave =="1803":
            retiro = int(input("¿cual es el monto a retirar?: "))
            if retiro >= 1 and retiro <= 100000:
                total = cuenta - retiro
                total_2 = cajero - retiro
                print("saldo cuenta=",total)
                print("saldo cajero=",total_2)
                break

            else:
                print("no es posible retirar esa cantidad.")
                break
            

    else:
        print("clave invalida")
        if (intento == 3):
            print("tarjeta bloqueada")
            break      