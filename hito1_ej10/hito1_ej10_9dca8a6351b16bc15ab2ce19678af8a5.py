if __name__=="__main__":
    cajero = 1000000
    lsalida= []
    cuenta = 100000
    intentos = 0
    monto = 0
    usuario=input("ingrese el usuario: ")
    clave = input("Ingrese la clave: ")
    continuar = ""
    while continuar!="N":
        while intentos!=0 and clave!="1803" and usuario!="10334151":
            intentos+=1
            if intentos==3:
                print("tarjeta bloqueada")
                quit()
            usuario=int(input("ingrese el usuario: "))
            clave=int(input("ingrese la clave: "))
        if clave=="1803" and usuario=="10334151":
            monto= int(input("monto a retirar:"))
            if monto<=cuenta:
                cuenta-=monto
                cajero-=monto
                lsalida.append("saldo cuenta="+str(cuenta))
                lsalida.append("saldo cajero="+str(cajero))
            else:
                lsalida.append("monto no permitido")
        continuar=(input("desea continuar?"))
        print(lsalida)