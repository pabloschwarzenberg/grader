#Cajero Automático
from time import sleep
s_c= 1000000
s_u= 100000
a=str(int(input("Ingrese usuario:")))
p=str(int(input("Ingrese password:")))
while True:
    if(a=="10334151" and p== "1803"):
        print("VALIDO")
        sleep(1)
        rr=int(input("Ingrese cuanto quiere retirar:"))
        if(rr>s_u and rr>s_c):
            print("NO PERMITIDO")
            break
        if(rr<s_u and rr<s_c):
            s_uu=s_u-rr
            s_cu=s_c-rr
            print("saldo cuenta=", s_uu)
            print("saldo cajero=", s_cu)
            mk=int(rr/20000)
            rr=rr%20000
            mk1= int(rr/10000)
            rr=rr%10000
            mk2=int(rr/5000)
            rr=rr%5000
            print("BILLETES 20000= ", mk)
            print("BILLETES 10000= ", mk1)
            print("BILLETES 5000= ", mk2)
        if(rr!="m"):
            break