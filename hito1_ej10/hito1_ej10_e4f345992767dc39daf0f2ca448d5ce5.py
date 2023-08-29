#Cajero Automático
sc=1000000
si=100000
s=0
i=2

c = int(input("Ingrese su contraseña: "))

while i != 0:
    if c != 1803:
        print("clave invalida")
        i=i-1
        c=int(input("Porfavor ingrese su contraseña: "))
    else:
        m=int(input("Ingrese el monto a retirar de su cuenta (sin puntos): "))
        if m < si:
            s=si-m
            sc=sc-m
            print("saldo cuenta=", s)
            print("saldo cajero=", sc)
            break
        else:
            print("monto no permitido")
if i==0:
    print("tarjeta bloqueada")      