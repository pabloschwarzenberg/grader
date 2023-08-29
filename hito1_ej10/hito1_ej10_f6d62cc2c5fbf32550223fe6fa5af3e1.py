#Cajero Automático
x=int(input("ingrese el usuario:"))
y=int(input("ingrese la clave:"))
Cajero=1000000
usuario=100000
intentos = 0
while intentos <= 1:
    if intentos == 0:
        print("Usuario")
        input()
        print("clave")
        clave = input()
        if clave == "1803":
            c = 1
        elif intentos == 2:
            print("Tarjeta bloqueada")
            break
        else:
            intentos += 1
    elif c == 1:
        print("Ingrese monto a retirar")
        p = input()
        di = "qwertyuiopñlkjhgfdsazxcvbm,.-{}+´¿QWERTYUIOPÑLKJHGFDSAZXCVBM"
        if p in di:
            break
        elif p == "N":
            c = 1
        else:
            Monto(float(p))
       
if monto > Cajero:
   return "Monto no permitido"
else:
   usuario = usuario-monto
   Cajero = Cajero-monto
   print("saldo cuenta=",usuario)
   print("saldo cajero=",Cajero)
   return [usuario,Cajero]

       