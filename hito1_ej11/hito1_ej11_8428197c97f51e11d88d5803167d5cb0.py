#Cajero Automático
saldo_total = 1000000
billetes_20000 = 20
billetes_10000 = 40
billetes_5000 = 40

# Pedir al usuario el monto a retirar
monto_retiro = int(input("Ingrese el monto que desea retirar: "))

# Verificar que el monto sea menor o igual al saldo disponible
if monto_retiro <= saldo_total:
  
  # Calculamos la cantidad de cada billete a entregar
  cant_20000 = min(monto_retiro // 20000, billetes_20000)
  monto_retiro -= cant_20000 * 20000
  cant_10000 = min(monto_retiro // 10000, billetes_10000)
  monto_retiro -= cant_10000 * 10000
  cant_5000 = min(monto_retiro // 5000, billetes_5000)
  monto_retiro -= cant_5000 * 5000
  
  # Si el monto sobrante es mayor a 0, entonces no se puede entregar la cantidad solicitada
  if monto_retiro > 0:
      print("No hay suficiente cantidad de billetes para el monto solicitado")
  else:
      # Actualizamos el saldo y los billetes disponibles, e imprimimos el resultado
      saldo_total -= (cant_20000*20000 + cant_10000*10000 + cant_5000*5000)
      billetes_20000 -= cant_20000
      billetes_10000 -= cant_10000
      billetes_5000 -= cant_5000
      print("Retirando", cant_20000, "billetes de 20.000, ", cant_10000, "billetes de 10.000 y ", cant_5000, "billetes de 5.000")
      print("Saldo disponible:", saldo_total)
      print("Billetes de 20.000 disponibles:", billetes_20000)
      print("Billetes de 10.000 disponibles:", billetes_10000)
      print("Billetes de 5.000 disponibles:", billetes_5000)
else:
    # Si el monto a retirar es mayor al saldo disponible, entonces no se puede realizar la transacción
    print("No hay suficiente saldo en la cuenta para el retiro solicitado")      