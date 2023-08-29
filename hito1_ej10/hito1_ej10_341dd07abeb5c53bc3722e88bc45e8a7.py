#Cajero Automático
a=float(input("Ingrese su usuario: "))
b=float(input("Ingrese su contraseña: "))


while b!= 1803:
    print("Clave invalida")
    b = float(input("\nIngrese su contraseña: "))
    print("Clave invalida")
    b = float(input("\nCongrese su contraseña: "))

    print("\nTarjeta Bloqueada")
    break
c=float(input("Ingrese el monto que desea retiar: "))
d=1000000-c
if d==955000:
    print("saldo cuenta=55000")
    print("saldo cajero=955000")
    if d!=955000:
        print("monto no permitido")     