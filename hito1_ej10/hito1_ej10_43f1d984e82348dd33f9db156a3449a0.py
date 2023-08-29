i=0
while i<3:
    saldo_cajero=1000000
    saldo_cuenta=100000
    usuario=int(input())
    clave=int(input())
    if usuario==10334151 and clave==1803:
        monto=int(input("Indique monto a sacar: "))
        if monto>100000:
            print("monto no permitido")
            continue
        elif monto<=100000:
            saldo_cajero=saldo_cajero-monto
            saldo_cuenta=saldo_cuenta-monto
            print("saldo cuenta=",saldo_cuenta)
            print("saldo cajero=",saldo_cajero)
            continuidad=input()
            if continuidad=="N":
                continue
            else:
                break
    else:
        print("clave inválida")
        i+=1
if i==3:
    print("clave bloqueada")
