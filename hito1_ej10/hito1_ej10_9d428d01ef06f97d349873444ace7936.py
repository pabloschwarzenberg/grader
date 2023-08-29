#Cajero Automático
pregunta1=int(input("Ingrese numero de usuario: "))
pregunta2=int(input("Ingrese clave: "))

if pregunta1==10334151 and pregunta2==1803:
    respuesta1=int(input("Ingrese monto a retirar: "))
    if respuesta1<=100000:
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
                print("saldo cuenta=",100000-respuesta1)
                print("saldo cajero=",1000000-respuesta1)
            else:
                print("Monto no permitido")
        else:
            print("Tarjeta bloqueada")


