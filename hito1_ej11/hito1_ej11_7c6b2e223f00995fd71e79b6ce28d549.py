cajero=1000000
b20=20
b10=40
b5=40
cuenta=100000
intentos=0
clave_c=False
monto_c=False
clave=""
monto=""

while clave!="Y" and intentos!=3 and monto!="Y":
    usuario=input("Ingrese usuario")
    clave=input("Ingrese clave")
    if clave!="1803" and clave!="Y":
        print("clave invalida")
        intentos+=1
    if intentos==3:
        print("tarjeta bloueada")
    if clave=="1803":
        while monto!="Y":
            monto=input("Monto a retirar: ")
            if monto!="Y":
                monto=int(monto)
                if monto<=cajero and monto<=cuenta:
                    cajero=cajero-monto
                    cuenta=cuenta-monto
                    if monto>=35000:
                        monto=monto-35000
                    n=monto//20000
                    a=(monto-20000*n)//10000
                    r=(monto-20000*n-10000*a)//5000
                    b20=b20-n-1
                    b10=b10-a-1
                    b5=b5-r-1
                    n+=1
                    a+=1
                    r+=1
                    print("[saldo cuenta = ",cuenta, "saldo cajero = ",cajero)
                    print("billetes 20000= ",n,"billetes 10000= ",a,"billetes 5000= ",r) 
                else:
                    print("monto no permitido")