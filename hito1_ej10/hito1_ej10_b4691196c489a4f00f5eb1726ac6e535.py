#Cajero Automático
# Definir el usuario, la clave y el saldo inicial del cajero
usuario_cajero = "10334151"
clave_cajero = "1803"
saldo_cajero = 1000000

# Definir los contadores de intentos fallidos y continuar
intentos_fallidos = 0
continuar = True

# Loop principal del cajero automático
while continuar:

  # Pedir usuario y clave para ingresar
  usuario = input("Ingrese su usuario: ")
  clave = input("Ingrese su clave: ")

  # Verificar que el usuario y la clave sean correctos
  if usuario == usuario_cajero and clave == clave_cajero:
    
    # Si la clave es correcta, pedir el monto a retirar
    monto = float(input("Ingrese el monto a retirar: "))
    
    # Verificar que el monto sea válido
    if monto <= saldo_cajero and monto <= 100000 and monto % 10000 == 0:

      # Actualizar los saldos y mostrar el nuevo saldo del cajero y el usuario
      saldo_cajero -= monto
      saldo_usuario = 100000 - monto
      print("Retiro exitoso.")
      print("Saldo cuenta = {}".format(saldo_usuario))
      print("Saldo cajero = {}".format(saldo_cajero))

    else:
      # Notificar al usuario que el monto no es válido
      print("Monto no permitido.")

  else:
    # Notificar al usuario que la clave no es válida y aumentar el contador de intentos fallidos
    print("Clave invalida.")
    intentos_fallidos += 1

    if intentos_fallidos == 3:
      # Si se han realizado 3 intentos fallidos, bloquear la tarjeta y salir del programa
      print("Tarjeta bloqueada.")
      continuar = False

  # Preguntar si el usuario desea continuar
  continuar_respuesta = input("¿Desea continuar? (S/N)")

  if continuar_respuesta == "N":
    # Si el usuario ingresa "N", salir del programa
    continuar = False
