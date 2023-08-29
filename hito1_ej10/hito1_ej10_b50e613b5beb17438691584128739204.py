#Cajero Automático
while True:
    usuario=float(input("Ingrese nombre de usuario:"))
    clave=float(input("Ingrese su clave:"))
    saldoinicial=100000
    cajeroinicial=1000000
    i=0
    if clave!=1803:
        if i<=1:
            print("clave invalida")
            continue
        elif 2>=i>1:
            print("tarjeta bloqueada")
            break
        i=i+1

    elif usuario==10334151 and clave==1803 and i<3:
        a=float(input("Ingrese monto a retirar:"))
        if a<100000:
            print("saldo cuenta=",int(saldoinicial-a))
            print("saldo cajero=",int(cajeroinicial-a))
            b=input("Para salir ingrese una letra distinta a N:")
            b=str(b)
            if b!="N":
                break
            i=i+1

        elif a>100000:
            print("monto no permitido")      