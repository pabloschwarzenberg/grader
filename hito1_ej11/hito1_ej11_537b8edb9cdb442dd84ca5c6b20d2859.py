saldo_cajero=1000000
saldo_usuario=100000
billetes_20=20
billetes_10=40
billetes_5=40
usuario=input("ingrese usuario: ")
usuario_invalido=True
while usuario_invalido:
    if usuario=="10334151":
        usuario_invalido=False
    else:
        print("usuario invalido")
        usuario=input("ingrese usuario: ")
if usuario=="10334151":
    clave_invalida=True
    clave=input("ingrese clave: ")
    intentos=3

    while clave_invalida and intentos>1:
       if clave=="1803":
           clave_invalida=False
       else:
           print("clave invalida")
           clave=input("ingrese clave: ")
           intentos=intentos-1
    

          

if clave=="1803":
    monto=input("ingrese monto a retirar: ")
    monto=int(monto)
    monto_invalido=True
    while monto_invalido:
        if monto>saldo_cajero or monto>saldo_usuario:
           print("monto no permitido")
           monto=input("ingrese monto retirar :")
           monto=int(monto)
        else:
            monto_invalido=False
            saldo_cajero=saldo_cajero-monto
            saldo_usuario=saldo_usuario-monto
            print("saldo cajero=",saldo_cajero)
            print("saldo cuenta=",saldo_usuario)
            n_de20=0
            a=0
            n_de5=0
            if monto>20000:
                sacar_de_20=True
            
            
                while sacar_de_20 and billetes_20>0:
                         if 20000>monto:
                                sacar_de_20=False
                         else:
                              monto=monto-20000
                              billetes_20=billetes_20-1
                              n_de20=n_de20+1
                              
                                
            if 20000>monto>10000:
                sacar_de_10=True
            
                while sacar_de_10 and billetes_10>0:
                    if 10000>monto:
                        sacar_de_10=False
                    else:
                        monto=monto-10000
                        billetes_10=billetes_10-1
                        a=a+1
                        
            
            if 10000>monto>0:
                        sacar_de_5=True
                        
                        while sacar_de_5 and billetes_5>0:
                            if monto==0:
                                sacar_de_5=False
                            else:
                                 monto=monto-5000
                                 billetes_5=billetes_5-1
                                 n_de5=n_de5+1
                            

print("billetes 20000=",n_de20)
print("billetes 10000=",a)
print("billetes 5000=",n_de5)


                        
        
                    
if intentos==1:
    print("tarjeta bloqueada: ")