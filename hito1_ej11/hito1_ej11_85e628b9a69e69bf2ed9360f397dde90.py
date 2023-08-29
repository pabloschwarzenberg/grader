#Cajero Automático
import sys

a=input("Ingrese usuario: ")
b=input("Ingrese clave: ")
c=0
s=1000000
while b!="1803":
    c+=1
    if c==3:
        print("tarjeta bloqueada")
        sys.exit(1)
    else:
        print("clave incorrecta")
        b=input("Ingrese clave: ")
m=int(input("Monto a retirar: "))
if m>100000:
    print("Monto no permitido")
else:
    cajero=s-m
    cuenta=100000-m
    print("saldo cuenta=",cuenta)
    print("saldo cajero=",cajero)
    g=m//20000
    f=m%20000
    h=f//10000
    j=f%10000
    k=j//5000
    print("billetes 20000=",g)
    print("billetes 10000=",h)
    print("billetes 5000=",k)