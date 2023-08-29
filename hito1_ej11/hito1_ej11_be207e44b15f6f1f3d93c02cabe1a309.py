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
# Definir las cantidades iniciales de cada tipo de billete
billetes_20000 = 20
billetes_10000 = 40
billetes_5000 = 40

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
      # Calcular la cantidad de billetes de cada tipo que se necesitan para el retiro
      # Inicializar las variables en cero
      b_20000 = 0
      b_10000 = 0
      b_5000 = 0
      # Mientras el monto sea mayor o igual a 20000 y haya billetes de ese tipo disponibles
      while monto >= 20000 and billetes_20000 > 0:
        # Restar un billete de 20000 al monto y a la cantidad disponible
        monto -= 20000
        billetes_20000 -= 1
        # Sumar un billete de 20000 a la cantidad a entregar
        b_20000 += 1
      # Mientras el monto sea mayor o igual a 10000 y haya billetes de ese tipo disponibles
      while monto >= 10000 and billetes_10000 > 0:
        # Restar un billete de 10000 al monto y a la cantidad disponible
        monto -= 10000
        billetes_10000 -= 1
        # Sumar un billete de 10000 a la cantidad a entregar
        b_10000 += 1
      # Mientras el monto sea mayor o igual a 5000 y haya billetes de ese tipo disponibles
      while monto >= 5000 and billetes_5000 > 0:
        # Restar un billete de 5000 al monto y a la cantidad disponible
        monto -= 5000
        billetes_5000 -= 1
        # Sumar un billete de 5000 a la cantidad a entregar
        b_5000 += 1
      
      # Si el monto quedó en cero, se pudo hacer el retiro con los billetes disponibles  
      if monto == 0:
        # Actualizar los saldos del cajero y de la cuenta restando el total del retiro (sin los billetes)
        saldo_cajero -= (b_20000 * 20000 + b_10000 * 10000 + b_5000 * 5000)
        saldo_cuenta -= (b_20000 * 20000 + b_10000 * 10000 + b_5000 * 5000)
        # Imprimir los nuevos saldos y la cantidad de billetes entregados
        print("saldo cuenta =", saldo_cuenta)
        print("saldo cajero =", saldo_cajero)
        print("billetes 20000 =", b_20000)
        print("billetes 10000 =", b_10000)
        print("billetes 5000 =", b_5000)
      else:
        # Imprimir un mensaje de error indicando que no hay suficientes billetes para el retiro
        print("No hay suficientes billetes para el retiro")
    else:
      # Imprimir un mensaje de error indicando que el monto no es válido
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
