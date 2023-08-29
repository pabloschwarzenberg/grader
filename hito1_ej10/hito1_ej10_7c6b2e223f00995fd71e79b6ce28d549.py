cajero=1000000
cuenta=100000
intentos=0
clave_c=False
monto_c=False
clave=""
monto=""

while clave!="Y" and intentos!=3 and monto!="Y":
    usuario=input("Ingrese usuario")
    clave=input("Ingrese clave")
    if clave!="1803" and clave!="S":
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
                    print("saldo cuenta = ",cuenta, "saldo cajero = ",cajero)
                else:
                    print("monto no permitido")
                