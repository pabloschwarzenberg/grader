#Cajero Automático
n="n"
saldo_cajero=1000000
saldo_cuenta=100000
while(n!="N"):
    k=0
    User=int(input("Ingrese su número de usuario: "))
    Password=0
    if(User==10334151):
        while(Password!=1803):
            Password=int(input("Ingrese su número secreto: "))
            if(Password!=1803):
                print("clave invalida")
                k+=1
            if(k>=3):
                print("tarjeta bloqueada")
                break
        if(k>=3):
            break
        Monto=int(input("Ingrese monto a retirar: "))
        if((Monto<=saldo_cuenta)and(Monto<=saldo_cajero)):
            saldo_cuenta-=Monto
            saldo_cajero-=Monto
            print("saldo cuenta=",saldo_cuenta,sep="")
            print("saldo cajero=",saldo_cajero,sep="")
            n=input("Ingrese \"N\" para finalizar; ingrese cualquier otro valor para continuar: ")
        else:
            print("monto no permitido")
            break