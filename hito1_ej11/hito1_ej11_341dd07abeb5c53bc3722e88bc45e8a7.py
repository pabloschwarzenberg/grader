#Cajero Automático
a=float(input("Ingrese su usuario: "))
b=float(input("Ingrese su contraseña: "))


while b!= 1803:
    print("Clave invalida")
    b = float(input("\nIngrese su contraseña: "))
    print("Clave invalida")
    b = float(input("\nIngrese su contraseña: "))

    print("\nTarjeta Bloqueada")
    break


c=int(input("Ingrese el monto que desea retiar: "))
d=1000000-c

if d==d:
    print("saldo cuenta=",100000-c)
    print("saldo cajero=",1000000-c)
    if c>=20000:
          queda=c//20000
          print("billetes 20000=",int(queda))
          c= c%20000

    if c >= 10000:
          queda = c // 10000
          print("billetes 10000=",int(queda))
          c = c % 10000

    if c >= 5000:
          queda = c // 5000
          print("billetes 5000=",int(queda))
          c = c % 5000

    if d!= d:
        print("monto no permitido")
