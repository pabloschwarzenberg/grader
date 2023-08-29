i = 0
while i<3:
    x=int(input("Ingrese su usuario:"))
    y=int(input("Ingrese su clave:"))
    if x==10334151 and y!=1803:
        print("Clave Invalida")
    else:
        m=int(input("Ingrese el monto a retirar:"))
        break
    i+=1
if i==3:
    print("Tarjeta bloqueada")

dineros=1000000
monto= dineros-m
saldo_cuenta=100000
saldo_final=saldo_cuenta-m
if m>100000:
    print("Monto no permitido")
elif m<=100000:
    print("Saldo Cajero=",monto)
    print("Saldo Cuenta=",saldo_final)
