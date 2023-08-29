#Cajero Automático
# vars del nivel 1
bal_cuenta=100000
bal_cajero=1000000
intentos=0
# stock disponible
BD_20K=20
BD_10K=40
BD_5K=40
# BD= Billetes Disponible
# CR= Cantidad Retiro (se podia hacer con lista pero muy complicado)
# CRB= Cantidad Retiro Billetes _20K,10K,5K
while(True):
    username=input("Ingrese su usuario: ")
    password=input("Ingrese su clave: ")
    if(username=="10334151" and password=="1803"):
        break
    else:
        intentos+=1
        if(intentos>=3):
            print("Tarjeta bloqueada.")
            exit()
        print("Clave inválida. Intente denuevo.")

while(True):
    CR=int(input("Ingrese el monto a retirar: "))
    if(CR<=0):
        print("Monto no permitido. Intente denuevo.")
    elif(CR>bal_cuenta):
        print("Saldo insuficiente. Intente denuevo.")
    else:
        # se me habia olvidao estos 2
        bal_cuenta-=CR
        bal_cajero-=CR
        CRB_20K=CR // 20000
        if(CRB_20K>BD_20K):
            CRB_20K=BD_20K
        CR-=CRB_20K*20000
        BD_20K-=CRB_20K
        print("Billetes 20000 =",CRB_20K)
        # 10 LUCA
        CRB_10K=CR // 10000
        if(CRB_10K>BD_10K):
            CRB_10K=BD_10K
        CR-=CRB_10K*10000
        BD_10K-=CRB_10K
        print("Billetes 10000 =", CRB_10K)
        # 5 LUCA
        CRB_5K=CR // 5000
        if(CRB_5K>BD_5K):
            CRB_5K=BD_5K
        CR-=CRB_5K*5000
        BD_5K-=CRB_5K
        print("Billetes 5000 =", CRB_5K)
        bal_cuenta-=CR
        bal_cajero-=CR
        print("saldo cuenta=",bal_cuenta)
        print("saldo cajero=",bal_cajero)
        # si no me equivoqué con el // toi dao
    opcion=input("desea salir?(S/N)")
    if(opcion.upper()!="N"):
        break