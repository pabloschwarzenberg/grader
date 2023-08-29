usuario=""
clave=""
op=3
while op>0 and (usuario!="10334151" or clave!="1803"):
    usuario=input("usuario: ")
    clave= input("clave: ")
    if usuario!="10334151" and clave!="1803":
        print("clave invalida")
        op-=1
    if op==0:
        print("tarjeta bloqueada")
        
if usuario=="10334151" and clave=="1803":
    seguir="N"
    saldo_cajero=1000000
    saldo_cuenta=100000
    bte20=20
    bte10=40
    bte5=40
    while seguir =="N":
        dinero=int(input("monto a retirar: "))
        entrega_bte20=0
        entrega_bte10=0
        entrega_bte5=0
        if dinero>saldo_cuenta or dinero>saldo_cajero or dinero<0 or dinero%5000!=0:
            print("monto no permitido")
        else:
            suma_billetes=0
            while suma_billetes!=dinero:

                por_entregar=dinero-suma_billetes
                
                if por_entregar%5000==0 and suma_billetes!=dinero:
                    entrega_bte5+=1
                    bte5-=1
                    suma_billetes+=5000
                    por_entregar-=5000
                    
                if por_entregar%20000==0 and suma_billetes!=dinero:
                    entrega_bte20+=1
                    bte20-=1
                    suma_billetes+=20000  
                    por_entregar-=20000                    
                    
                if por_entregar%10000==0 and suma_billetes!=dinero:
                    entrega_bte10+=1
                    bte10-=1
                    suma_billetes+=10000
                    por_entregar-=10000
                    

                    
            saldo_cajero-=dinero
            saldo_cuenta-=dinero
            print("saldo cuenta="+str(saldo_cuenta))
            print("saldo cajero="+str(saldo_cajero))
            print("billetes 20000="+str(entrega_bte20))
            print("billetes 10000="+str(entrega_bte10))
            print("billetes 5000="+str(entrega_bte5))
        seguir= input("continuar N: ")
      