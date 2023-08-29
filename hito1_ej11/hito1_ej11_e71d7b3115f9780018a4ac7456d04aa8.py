#Cajero Automático
usuario = int(input("Ingrese el número de usuario: "))

while usuario!=10334151:
        print("Error. Usuario no válido")
        usuario = int(input("Ingrese el número de usuario: "))

clave = int(input("Ingrese el clave: "))
        
saldo = 1000000
cuenta = 100000

intentos = 0 
while clave!=1803:
    if intentos ==3:
        print("Error. Tarjeta Bloqueada")
        print("Intento",intentos)
        break
    else: 
        intentos = intentos + 1
        print("Error. Clave invalida")
        print("Intento",intentos)
        clave = int(input("Ingrese clave: "))
        
if intentos != 3 :
    print("Monto a retirar")
    monto = int(input("Ingrese el monto a retirar: "))
    if monto <= cuenta:
        totalcuenta = cuenta-monto
        totalsaldo = saldo-monto
        print("saldo cuenta=",totalcuenta)
        print("saldo cajero=",totalsaldo)
        for billete in [20000,10000,5000]:
            canbille = monto //billete
            sobrante = monto %billete          
            if canbille !=0:
                print("billetes",billete,"=", canbille)
                monto = sobrante
              
    else:
        print("monto no permitido")