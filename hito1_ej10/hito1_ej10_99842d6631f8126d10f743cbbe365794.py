#Cajero Automático
from time import sleep
s_c = 1000000
s_u = 100000
a=str(int(input("Ingrese usuario: ")))
p=str(int(input("Ingrese password: ")))
while True:
    if(a=="10334151" and p=="1803"):
        print("VALIDO")
        sleep(1)
        rr=int(input("Ingrese cuanto quiere retirar: "))
        if(rr>s_u and rr>s_c):
            print("NO PERMITIDO")
            break
        if(rr<s_u and rr<s_c):
            s_uu=s_u-rr
            s_cu=s_c-rr
            print("saldo cuenta=", s_uu)
            print("saldo cajero=", s_cu)
        if(rr!="m"):
            break
    if(a!="10334151" or p!="1803"):
        print("clave invalida")
        sleep(1)
        print("INTENTO NUMERO 2")
        sleep(1)
        p= str(int(input("Ingrese password:")))
        if(a!="10334151" or p!= "1803"):
            print("clave invalida")
            sleep(1)
            print("INTENTO NUMERO 3")
            sleep(1)
            p= str(int(input("Ingrese password:")))
            if(a!="10334151" or p!="1803"):
                print("tarjeta bloqueada")
                break