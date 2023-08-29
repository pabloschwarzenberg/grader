#Cajero Automático
saldo_cajero=1000000
saldo_cuenta=100000
intentos=3
clave_invalida=True  
usuario_invalido=True
usuario=input("Ingrese usuario: ")
clave=input("Ingrese clave: ") 
while clave_invalida and usuario_invalido and intentos>1:
    if clave=="1803" and usuario=="10334151":
        clave_invalida=False
    else:
        clave_invalida=True 
        usuario_invalido=True
        intentos=intentos-1
        print("intentos restantes: "+str(intentos))
        clave=input("Ingrese clave: ")
if clave=="1803" and usuario=="10334151":
    monto=int(input("Ingrese monto a retirar: ")) 
    if monto<1000000:
      saldo_cajero=saldo_cajero-monto
      saldo_cuenta=saldo_cuenta-monto
      print("saldo cuenta="+str(saldo_cuenta))
      print("saldo cajero="+str(saldo_cajero))
    else:
        print("monto no permitido")
else:
    print("Tarjeta bloqueada") 

