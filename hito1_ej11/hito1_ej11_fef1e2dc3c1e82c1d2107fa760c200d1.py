#Cajero Automático
Saldo_Cajero=1000000
Cantidad_Cajero_20000=20
Cantidad_Cajero_10000=40
Cantidad_Cajero_5000=40
billete_20000=20000
billete_10000=10000
billete_5000=5000
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
    Cantidad_sobrante=Monto_retirar//20000
    Cantidad_Billetes20000=Cantidad_sobrante
    Resta1=Cantidad_Billetes20000*billete_20000
    Monto_retirar=Monto_retirar-Resta1

    Cantidad_sobrante=Monto_retirar//10000
    Cantidad_Billetes10000=Cantidad_sobrante
    Resta2=Cantidad_Billetes10000*billete_10000
    Monto_retirar=Monto_retirar-Resta2

    Cantidad_sobrante=Monto_retirar//5000
    Cantidad_Billetes5000=Cantidad_sobrante
    Resta3=Cantidad_Billetes5000*billete_5000
    Monto_retirar=Monto_retirar-Resta3

    Saldo_Cajero=Saldo_Cajero-(Resta1+Resta2+Resta3)
    Saldo_cuenta=Saldo_cuenta-(Resta1+Resta2+Resta3)

    print("billetes 20000=",Cantidad_Billetes20000)
    print("billetes 10000=",Cantidad_Billetes10000)
    print("billetes 5000=",Cantidad_Billetes5000)
    print("saldo cajero=",Saldo_Cajero)
    print("saldo cuenta=",Saldo_cuenta)

    break     