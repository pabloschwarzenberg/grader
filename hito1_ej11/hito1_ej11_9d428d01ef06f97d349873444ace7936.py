#Cajero Automático
pregunta1=int(input("Ingrese numero de usuario: "))
pregunta2=int(input("Ingrese clave: "))

if pregunta1==10334151 and pregunta2==1803:
    respuesta1=int(input("Ingrese monto a retirar: "))
    if respuesta1<=100000:
        respuesta2=respuesta1%10000
        if respuesta2%10000==0:
            respuesta3=respuesta1/10000
            print("billetes 20000=0")
            print("billetes 10000=",int(respuesta3))
            print("billetes 5000=0")
        else:
            respuesta4=respuesta1-5000
            respuesta5=respuesta4/10000
            print("billetes 20000=",0)
            print("billetes 10000=", int(respuesta5))
            print("billetes 5000=",1)
        print("saldo cuenta=",100000-respuesta1)
        print("saldo cajero=",1000000-respuesta1)
    else:
        print("Monto no permitido")
else:
    print("Clave invalida")
    pregunta1=int(input("Ingrese numero de usuario: "))
    pregunta2=int(input("Ingrese clave: "))
    if pregunta1==10334151 and pregunta2==1803:
        respuesta1=int(input("Ingrese monto a retirar: "))
        if respuesta1<=100000:
            respuesta2 = respuesta1 % 10000
            if respuesta2 % 10000==0:
                respuesta3 = respuesta1 / 10000
                print("billetes 20000=0")
                print("billetes 10000=", int(respuesta3))
                print("billetes 5000=0")
            else:
                respuesta4 = respuesta1 - 5000
                respuesta5 = respuesta4 / 10000
                print("billetes 20000=", 0)
                print("billetes 10000=", int(respuesta5))
                print("billetes 5000=", 1)
            print("saldo cuenta=",100000-respuesta1)
            print("saldo cajero=",1000000-respuesta1)
        else:
            print("Monto no permitido")
    else:
        print("Clave invalida")
        pregunta1=int(input("Ingrese numero de usuario: "))
        pregunta2=int(input("Ingrese clave: "))
        if pregunta1==10334151 and pregunta2==1803:
            respuesta1=int(input("Ingrese monto a retirar: "))
            if respuesta1<=100000:
                respuesta2 = respuesta1 % 10000
                if respuesta2 % 10000==0:
                    respuesta3 = respuesta1 / 10000
                    print("billetes 20000=0")
                    print("billetes 10000=", int(respuesta3))
                    print("billetes 5000=0")
                else:
                    respuesta4 = respuesta1 - 5000
                    respuesta5 = respuesta4 / 10000
                    print("billetes 20000=", 0)
                    print("billetes 10000=", int(respuesta5))
                    print("billetes 5000=", 1)
                print("saldo cuenta=",100000-respuesta1)
                print("saldo cajero=",1000000-respuesta1)
            else:
                print("Monto no permitido")
        else:
            print("Tarjeta bloqueada")
    