#Cajero Automático

intento=0
while intento<3:
    usuario=input("Usuario: ")
    clave=input("Clave: ")
    if usuario=="10334151" and clave=="1803":
        break
    else:
        print("clave invalida")
        intento=intento+1        
if usuario!="10334151" or clave!="1803":
    print("Tarjeta bloqueada")
else:
    saldo_inicial_persona=100000
    saldo_inicial_Cajero=1000000
    billete_20=20
    billete_10=40
    billete_5=40
    monto=input("Monto a retirar: ")
    while monto!="N":
       if int(monto)<=0 or int(monto)>saldo_inicial_Cajero or int(monto)>saldo_inicial_persona or int(monto)%5000!=0:
            print("monto no permitido")
       else:
            monto=int(monto)
            saldo_inicial_persona=saldo_inicial_persona-int(monto)
            saldo_inicial_Cajero=saldo_inicial_Cajero-int(monto)
            print("saldo cuenta=" + str(saldo_inicial_persona))
            print("saldo cajero="+str(saldo_inicial_Cajero))
            entregar=monto
            billete_20_entregado=0
            billete_10_entregado=0
            billete_5_entregado=0
            while entregar>0:
                if entregar%20000==0 and billete_20>0:
                        entregar-=20000
                        billete_20-=1
                        billete_20_entregado+=1
                elif entregar%10000==0 and billete_10>0:
                        entregar-=10000
                        billete_10-=1
                        billete_10_entregado+=1 
                elif entregar%5000==0 and billete_5>0:
                        entregar-=5000
                        billete_5-=1
                        billete_5_entregado+=1               
            print("billetes 20000=" + str(billete_20_entregado))
            print("billetes 10000=" + str(billete_10_entregado))
            print("billetes 5000=" + str(billete_5_entregado))
        monto=input("Monto a retirar: ")   
