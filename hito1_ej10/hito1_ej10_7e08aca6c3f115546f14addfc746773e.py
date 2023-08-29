#Cajero Automático
usuario=int(input("Ingrese numero de usuario: "))
clave=int(input("Ingrese su clave: "))

saldocajero=1000000
saldoinicial=100000

if usuario==10334151 and clave==1803:
  montoaretirar=int(input("Ingrese monto a retirar: "))
  if montoaretirar <= 100000:
    saldocajeroactualizado = saldocajero - montoaretirar
    saldocuenta = saldoinicial - montoaretirar
    print("Saldo de la cuenta es ", saldocuenta)
    print("Saldo cajero es ", saldocajeroactualizado)

  else:
    print("Monto no permitido")
    
else:
    print("clave invalida")
    clave=int(input("Ingrese nuevamente la clave: "))
    if clave==1803:
     montoaretirar=int(input("Ingrese monto a retirar: "))
     saldocajeroactualizado = saldocajero - montoaretirar
     saldocuenta = saldoinicial - montoaretirar
     print("Saldo de la cuenta es ", saldocuenta)
     print("Saldo cajero es ", saldocajeroactualizado) 
      
    else:
      print("tarjeta bloqueada")

    