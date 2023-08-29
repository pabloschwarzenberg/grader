#Cajero Automático
usuario = int(input("Ingrese el número de usuario: "))

while usuario!=10334151:
        print("Error. Usuario no válido")
        usuario = int(input("Ingrese el número de usuario: "))

clave = int(input("Ingrese el clave: "))
        
saldo = 1000000
cuenta = 100000

intento = 0 
while clave!=1803:
    if intento ==3:
        print("Error. Tarjeta Bloqueada")
        print("Intento",intento)
        break
    else: 
        intentos = intento + 1
        print("Error. Clave invalida")
        print("Intento",intento)
        clave = int(input("Ingrese clave: "))
        
if intento != 3 :
    print("Monto a retirar")
    monto = int(input("Ingrese el monto a retirar: "))
    if monto <= cuenta:
        totalcuenta = cuenta-monto
        totalsaldo = saldo-monto
        print("saldo cuenta=",totalcuenta)
        print("saldo cajero=",totalsaldo)
        for DINERO in [20000,10000,5000]:
            canmoneda = monto //DINERO
            sobrante = monto %DINERO          
            if canmoneda !=0:
                print("billetes",DINERO,"=", canmoneda)
                monto = sobrante
              
    else:
        print("monto no permitido")      