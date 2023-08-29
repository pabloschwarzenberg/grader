cj=1000000
b20=0
b10=0
b05=0
inf=0
while True:
    usuario=input("Ingrese usuario: ")
    clave=input("Ingrese su clave: ")
    sc=100000
    if usuario=="10334151" and clave=="1803":
        break
    else:
        inf+=1
        print("clave invalida")
        if inf==3:
            print("Tarjeta bloqueada.")
            exit()
while True:
    rt=int(input("ingrese monto a retirar: "))

    if rt>cj or rt>sc:
        print("fondos insuficientes")
    elif rt<=0:
        print("monto no permitido")
    else:
        scf=(sc-rt)
        cjf=(cj-rt)
        scfb=rt
        while scfb>0:
            if scfb>20000:
                scfb=scfb-20000
                b20=b20+1
            elif scfb>=10000:
                scfb=scfb-10000
                b10=b10+1
            elif scfb>=5000:
                scfb=scfb-5000
                b05=b05+1
        print("saldo cuenta=",scf)
        print("billetes 20000=",b20)
        print("billetes 10000=",b10)
        print("billetes 5000=",b05,"\n")
        print("saldo cajero=",cjf)
    opcion=input("¿Desea realizar otra transaccion?(ingrese cualquier tecla para salir o N para continuar): ")
    if opcion !="N":
        break