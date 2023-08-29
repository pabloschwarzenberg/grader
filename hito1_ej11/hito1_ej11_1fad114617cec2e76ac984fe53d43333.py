usuario=int(input("usuario"))
clave=int(input("clave"))
saldocajero=1000000
veinte=20
diez=40
cinco=40
ensucuenta=100000
contador=0
while contador<4:
    if clave==1803:
        monto=int(input("monto a retirar"))
        if monto<=ensucuenta and monto<=saldocajero:
            ensucuenta=ensucuenta-monto
            saldocajero=saldocajero-monto
            print("saldo cuenta="+str(ensucuenta)+"  "+"saldo cajero="+str(saldocajero))
            contador=8
            rveinte=monto//20000
            veinte=veinte-rveinte
            rdiez=(monto-20000*rveinte)//10000
            diez=diez-rdiez
            rcinco=(monto-20000*rveinte-10000*rdiez)//5000
            cinco=cinco-rcinco
            print("billetes 20000="+str(rveinte)+"\n"+"billetes 10000="+str(rdiez)+"\n"+"billetes 5000="+str(rcinco))
        else:
            print("monto no permitido")
    elif clave!=1803:
        contador=contador+1
        print("clave invalida")
if 3<contador<7 :
    print("tarjeta bloqueada")
      
      