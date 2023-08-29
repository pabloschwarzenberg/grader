#Cajero Automático
  intento=0

while intento < 4:
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
                billetes_20 = (total // 20000) - 1 
                billetes_10 = (total // 10000) - 3
                billetes_5 = (total // 5000) - 10
                
                print("saldo cuenta=",total)
                print("saldo cajero=",total_2)
                print("billetes 20000=",billetes_20)
                print("billetes 10000=",billetes_10)
                print("billetes 5000=",billetes_5)
                

                break
            else:
                print("no es posible retirar esa cantidad.")
                break
            

    else:
        print("clave invalida")
        if (intento == 3):
            print("tarjeta bloqueada")
            break    