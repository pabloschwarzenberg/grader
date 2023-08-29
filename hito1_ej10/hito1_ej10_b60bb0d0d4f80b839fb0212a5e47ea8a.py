print("Bienvenido a Banco PENTA")
U=input("Nº de usuario:")
C1=int(input("Ingrese su clave:"))
if C1==1803:
    M=int(input("Monto a retirar:"))
    if M<=100000:
        print("Monto permitido")
        print("Saldo cuenta=",100000-M)
        print("Saldo cajero=",1000000-M)
    else:
        print("Monto no permitido:")
if C1!=1803:
    print("Clave incorrecta intente denuevo")
    C2=int(input("Ingrese su clave:"))
    if C2==1803:
           M=int(input("Monto a retirar:"))
           if M<=100000:
               print("Monto permitido")
               print("Saldo cuenta=",100000-M)
               print("Saldo cajero=",1000000-M)
           else:
               print("Monto no permitido:")
    if C2!=1803:
        print("Clave incorrecta intente denuevo")
        C3=int(input("Ingrese su clave:"))
    if C3==1803:
           M=int(input("Monto a retirar:"))
           if M<=100000:
               print("Monto permitido")
               print("Saldo cuenta=",100000-M)
               print("Saldo cajero=",1000000-M)
           else:
               print("Monto no permitido:")
    if C3!=0:
        print("Tarjeta bloqueada")
    