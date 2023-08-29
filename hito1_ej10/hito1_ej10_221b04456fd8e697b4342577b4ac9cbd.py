#Cajero Automático
usuario=int(input("usuario"))
clave=int(input("Ingrese su clave (mire pa atras, le pueden estar robando su clave)"))
s1=100000
s2=1000000

f=0
while clave!=1803:
    print("clave invalida")
    f=f+1
    if f==3:
        print("tarjeta bloqueada")
        break
    clave=int(input("Ingrese su clave (mire pa atras, le pueden estar robando su clave)"))

if usuario==10334151  and clave==1803:
    retiro=int(input("monto a retirar"))
    s1=s1-retiro
    s2=s2-retiro
    if retiro>100000:
        print("monto no permitido")
    else:
        print("saldo cuenta=",s1)
        print("saldo cajero=",s2)
