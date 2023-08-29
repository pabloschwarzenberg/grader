#Cajero Automático
saldocajero=1000000
saldocuenta=100000
while True:
    usuario=str(input("ingrese usuario: "))
    if usuario=="n":
        break                            
    if usuario=="10334151":
        c=1
        while c<=3 :
            clave=str(input("ingrese clave"))
            if clave=="1803":
                monto=eval(input("monto a retirar : "))
                if saldocuenta-monto>0 :
                    saldocuenta=saldocuenta-monto
                    saldocajero=saldocajero-monto
                    print("saldo cuenta:",saldocuenta)
                    print("saldocajero:",saldocajero)
                    break
            else :
                print("clave invalida")
                c=c+1
        if c>3 :
            print("bloqueada")
            break
        
    
    