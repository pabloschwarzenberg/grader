#Cajero Automático
Saldo_Cajero=1000000
Saldo_cuenta=100000
Usuario=10334151
Clave=1803
contador=int(1)
inicio=True
while inicio:
  Validacion_usuario=int(input("Ingresar el nombre de Usuario:"))
  if Validacion_usuario==Usuario:
    print("Nombre de Usuario Valido")
    break
  elif Validacion_usuario!=Usuario:
    print("Nombre de Usuario Invalido")
    continue
while True:
  Validacion_Clave=int(input("Ingresar Clave:"))
  if Validacion_Clave==Clave:
    print("Clave valida")
    break
  elif Validacion_Clave!=Clave and contador == 3:
    print("Tarjeta bloqueada")
    break
  elif Validacion_Clave!=Clave:
    print("Clave invalida")
    contador=int(contador+1)
    print(contador)
    continue
while True:
  Monto_retirar=int(input("Ingresar el monto a retirar: "))
  
  if Monto_retirar>Saldo_cuenta:
    print("Monto invalido")
    continue
  elif Monto_retirar<=Saldo_cuenta:
    print("Monto Valido")
    Saldo_cuenta=Saldo_cuenta-Monto_retirar
    Saldo_Cajero=Saldo_Cajero-Monto_retirar
    print("saldo cuenta=",Saldo_cuenta)
    print("saldo cajero=",Saldo_Cajero)
    break