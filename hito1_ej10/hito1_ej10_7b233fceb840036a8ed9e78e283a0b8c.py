#Cajero Automático
Cajero_auto = 1000000
usuario = [10334151,1803,100000]
num1 = int(input("Ingrese usuario:"))
num2 = int(input("Ingrese clave:"))
us=[num1,num2]
count=1
lista=[0,0]
while us[1]!=usuario[1] and count<3:
    print("Clave invalida")
    b=int(input("Ingrese clave:")) 
    count=count+1
    if count==3 and b!=usuario[1]:
        print("Tarjeta bloqueada")
        break
while us[1]==usuario[1]and usuario[2]>0:
    c=(input("ingrese monto a retirar:"))
    if c=="Y":
        break
    if int(c)>usuario[2]:
        print("monto no permitido")
    if int(c)<=int(c):
        m=usuario[2]-int(c)
        usuario[2]=m
        Cajero_auto = Cajero_auto-int(c)
        num3 = str(usuario[2])
        num4 = str(Cajero_auto)
        lista[0]="saldo cuenta="+num3
        lista[1]="saldo cajero="+num4
        print(lista)           