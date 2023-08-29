#Cajero Automático
saldo_c=1000000
usuario1="10334151"
clave1="1803"
saldo_u=100000
contador=0
contador2=0

while True:
    usuario=input("numero de usuario:")
    clave=input("clave:")
    if usuario==usuario1 and clave==clave1:
        while True:
            monto=input("monto a retirar:")
            monto_int=int(monto)
            if monto_int>saldo_u:
                print("monto no permitido")
                contador2+=1
                if contador2>2:
                    break
                continue

            if monto_int>saldo_c:
                print("monto no permitido")
                contador2+=1
                if contador2>2:
                    break
                continue
            if monto_int<=saldo_c and monto_int<=saldo_u:
                saldo_u=saldo_u-monto_int
                saldo_c=saldo_c-monto_int
                print("saldo cuenta=",saldo_u,sep='')
                print("saldo cajero=",saldo_c,sep='')
                break
        continuar=input("Desea salir?")
        if continuar!="N":
          break
    elif clave1!=clave:
        print("clave invalida")
        contador+=1
        if contador>2:
            print("tarjeta bloqueada")
            break


