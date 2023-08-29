#Cajero Automático
saldo_cuenta=100000
saldo_cajero=1000000
Rut = int(input('Ingrese su Rut:'))
while Rut != 10334151:
  Rut = int(input('Rut invalido, intente nuevamente:'))
clave = int(input('Ingrese su clave:'))
if clave == 1803:
  print('Bienvenido')
  numero1 = int(input("Ingrese el monto a retirar, su saldo es de 100000: "))
  while numero1 > 100000:
    numero1 = int(input("Monto no permitido, intente nuevamente: "))
    if numero1 <= 100000:
      print("Retiro exitoso, su monto  actual es:",(saldo_cuenta - numero1))
      print("Saldo del cajero",(saldo_cajero - numero1))
      break
  if numero1 <=100000:
      print("Retiro exitoso, su monto actual es:",(saldo_cuenta - numero1))
      print("Saldo del cajero",(saldo_cajero - numero1))
else:
  clave = int(input('Clave invalido, intente nuevamente (2 intentos restantes):'))
  if clave == 1803:
    print('Bienvenido')
    numero1 = int(input("Ingrese el monto a retirar, su saldo es de 100000: "))
    while numero1 > 100000:
      numero1 = int(input("Monto no permitido, intente nuevamente: "))
      if numero1 <= 100000:
        print("Retiro exitoso, su monto actual es:",(saldo_cuenta - numero1))
        print("Saldo del cajero",(saldo_cajero - numero1))
        break
    if numero1 <=100000:
      print ("Retiro exitosos, su monto actual es:",(saldo_cuenta - numero1))
      print("Saldo del cajero:",(saldo_cajero - numero1))
  else:
    clave = int(input('Clave invalido, intente nuevamente (1 intentos restantes):'))
    if clave == 1803:
      print('Bienvenido')
      numero1 = int(input("Ingrese el monto a retirar, su saldo es de 100000: "))
      while numero1 > 100000:
        numero1 = int(input("Monto no permitido, intente nuevamente: "))
        if numero1 <= 100000:
          print("Retiro exitoso, su monto actual es:",(saldo_cuenta - numero1))
          print("Saldo del cajero",(saldo_cajero - numero1))
          break
      if numero1 <=100000:
        print ("Retiro exitosos, su monto actual es:",(saldo_cuenta - numero1))
        print("Saldo del cajero:",(saldo_cajero - numero1))
    else:
      print("Clave bloqueada, contáctese con su banco")