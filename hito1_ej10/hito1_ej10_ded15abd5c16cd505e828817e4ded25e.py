#Cajero Automático
cajero=1000000
cuenta=100000
n=1
usuario=int(input("Bienvenido, ingrese su rut sin digito verificador: "))
clave=int(input("Ingrese su clave: "))
while clave!=1803 and n<3:
    print("clave invalida")
    n=n+1
    clave=int(input("Ingrese su clave: "))
if n==3:
    print("tarjeta bloqueada")
else:
    monto=int(input("Ingrese el saldo a retirar: "))
    if monto>cajero or monto>cuenta:
        print("monto no permitido")
    else:
        cuenta=cuenta-monto
        cajero=cajero-monto
        print("saldo cuenta=",cuenta)
        print("saldo cajero=",cajero)

