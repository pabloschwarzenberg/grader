#Cajero Automático
def cajero():
    saldo_caja=1000000
    usuario=input("Ingresa tu usuario: ")
    if usuario=="10334151":
        saldo=100000
        i=0
        while i<3:
            clave=input("Ingresa tu clave:")
            if clave!="1803":
                print ("clave invalida")
                i+=1
            else:
                monto=int(input("Monto a retirar: "))
                if monto<saldo:
                    lista=[]
                    saldo=saldo-monto
                    saldo_caja=saldo_caja-monto
                    a="saldo cajero="+str(saldo_caja)
                    b="saldo cuenta="+str(saldo)
                    lista.append(b)
                    lista.append(a)
                    print(lista)
                    break
                else:
                    print("monto no permitido")
                    
cajero()
