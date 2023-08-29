#Cajero Automático
usuario= int(input("Ingrese numero de usuario: "))
while usuario != 10334151:
    usuario= int(input("\nError,ingrese usuario valido: "))
claveIngresada= int(input("\nIngrese su clave: "))


clave= 1803

saldoCajero= 1000000
saldoCuenta= 10000
i=0

    
while claveIngresada!=clave:
    print("\nclave invalida")
    claveIngresada= int(input("Ingrese su clave: "))
    i+=1
    if i>=3:
        print("\nTarjeta bloqueada")
        break
        
if claveIngresada==clave:
    montoR= int(input("\nIngrese monto a retirar: "))
    while montoR>saldoCajero:
        montoR= int(input("\nMonto no permitido, ingrese un monto valido: "))

saldoCuenta= saldoCuenta + montoR
saldoCajero= saldoCajero - montoR

print("saldo cuenta=",saldoCuenta)
print("\nsaldo cajero=",saldoCajero)      