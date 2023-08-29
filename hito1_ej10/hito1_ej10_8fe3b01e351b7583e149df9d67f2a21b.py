#Cajero Automático
#ingrese su usuario = 10334151
#ingrese clave = 1803
#retirar dinero
#salir
saldo_cajero = 1000000
saldo_cuenta = 100000

print("tienes 3 intentos para escribir los datos correctos")
contador = 1
while contador <=3:
    u = int(input("ingrese su usuario:"))
    c = int(input("ingrese su contraseña:"))
    if u == 10334151 and c == 1803:
        r = int(input("ingrese monto a retirar:"))
        if r > 100000:
         print("monto no permitido")
        if r <= 100000:
         sc = saldo_cuenta - r 
         scj = saldo_cajero - r
         print("saldo cuenta=",sc)
         print("saldo cajero=",scj)
         contador = 4
    
       
    else:
        print("clave invalida")
        if contador == 3:
            print("tarjeta bloqueada")
        contador = contador +1     
    