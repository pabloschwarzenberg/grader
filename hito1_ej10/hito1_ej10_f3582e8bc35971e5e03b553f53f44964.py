#Cajero Automático
clave="1803"
usuario="10334151"
us=input()
cv=input()
saldo=100000
cajero=1000000
if us==usuario:
    if cv==clave:
        monto=int(input())
        if monto<saldo:
            saldo=saldo-monto
            cajero=cajero-monto
        else:
           print("monto no permitido")
    else:
        i=0
        while i<3:
            cv=input()
            if cv==clave:
                monto=input()
                if monto<saldo:
                    saldo=saldo-monto
                else:
                    print("monto no permitido")
            i+=1
          
print("saldo cuenta=",saldo)
print("saldo cajero=",cajero)
            