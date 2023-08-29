#Cajero Automático
saldo_cuenta=100000
saldo_cajero=1000000
intentos=0

while(True):
    username=input("Ingrese su usuario: ")
    password=input("Ingrese su clave: ")
    if(username=="10334151" and password=="1803"):
        print("usuario passed")
        break # break pq condición de variable no me sirvió y ya taba chato
    else:
        intentos+=1
    if(intentos==3):
        print("Tarjeta bloqueada.")
        exit()
    print("Clave inválida. Intente nuevamente.")

while(True):
    monto_retiro=int(input("Ingrese el monto a retirar: "))
    if(monto_retiro<=0):
        print("Monto no permitido. Intente denuevo.")
    elif(monto_retiro>saldo_cuenta):
        print("Saldo insuficiente. Intente denuevo.")
    else:
        saldo_cuenta-=monto_retiro
        saldo_cajero-=monto_retiro
        print("Saldo cuenta=",saldo_cuenta)
        print("Saldo cajero=",saldo_cajero)
    opcion=input("quiere salir?")
    if(opcion.upper()!="N"):
        break