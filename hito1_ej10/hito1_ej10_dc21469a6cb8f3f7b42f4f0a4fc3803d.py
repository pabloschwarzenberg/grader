cj=1000000
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
        print("saldo cuenta=",scf)
        print("saldo cajero=",cjf)
    opcion=input("¿Desea realizar otra transaccion?(ingrese cualquier tecla para salir o N para continuar): ")
    if opcion !="N":
        break