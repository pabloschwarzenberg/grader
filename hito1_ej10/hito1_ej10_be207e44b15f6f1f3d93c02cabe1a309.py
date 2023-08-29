# Definir el usuario y la clave válidos
usuario_valido = "10334151"
clave_valida = "1803"
# Definir el saldo inicial del cajero y de la cuenta
saldo_cajero = 1000000
saldo_cuenta = 100000
# Definir una variable para controlar el número de intentos fallidos
intentos = 0
# Definir una variable para controlar si se desea continuar o no
continuar = "N"

# Mientras se desee continuar
while continuar == "N":
  # Pedir al usuario que ingrese su usuario y clave
  usuario = input("Ingresa tu usuario: ")
  clave = input("Ingresa tu clave: ")
  # Si el usuario y la clave son válidos
  if usuario == usuario_valido and clave == clave_valida:
    # Reiniciar el número de intentos fallidos
    intentos = 0
    # Pedir al usuario que ingrese el monto a retirar
    monto = int(input("Ingresa el monto a retirar: "))
    # Si el monto es válido (positivo, menor o igual al saldo de la cuenta y menor o igual al saldo del cajero)
    if monto > 0 and monto <= saldo_cuenta and monto <= saldo_cajero:
      # Actualizar los saldos del cajero y de la cuenta
      saldo_cajero -= monto
      saldo_cuenta -= monto
      # Imprimir los nuevos saldos
      print("saldo cuenta =", saldo_cuenta)
      print("saldo cajero =", saldo_cajero)
    else:
      # Imprimir un mensaje de error
      print("monto no permitido")
  else:
    # Incrementar el número de intentos fallidos
    intentos += 1
    # Si se superan los tres intentos fallidos
    if intentos == 3:
      # Imprimir un mensaje de bloqueo y salir del programa
      print("tarjeta bloqueada")
      break
    else:
      # Imprimir un mensaje de clave inválida
      print("clave inválida")
  # Preguntar al usuario si desea continuar o no
  continuar = input("¿Deseas continuar? (N/S): ")
