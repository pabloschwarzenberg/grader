#declaracion de variables
inicio = 'N'#si inicio es distinto de N el porgrama dejara de funcionar
intento = 0 #numero de intentos realizados para ingresar la contrasena de la cuenta
saldo_cuenta = 100000 #saldo de la cuenta
saldo_cajero = 1000000 #saldo del cajero
retirar_dinero = 0 #retirar dinero 1=si 0=no y como no hay usuario ni clave ingresada no se retirara dinero

while inicio == 'N': #mientras inicio sea n el programa se ejecutara
  user = int(input("Ingrese su usuario: "))
  if (user == 10334151):
    if(intento >= 3):
        print("Tarjeta bloqueada")
    else:
        print("Bienvenido!")
    while intento < 3:
      password = int(input("Ingrese su clave: "))
      if password == 1803:
        print("Clave correcta")
        print("saldo cuenta="+str(saldo_cuenta))
        print("saldo cajero="+str(saldo_cajero))
        retirar_dinero = 1
        break
      elif intento <= 2:
       print("Clave invalida")
       intento += 1
      if intento == 3:
        print("Tarjeta bloqueada")
  else:
    print("Usuario incorrecto")
  while retirar_dinero == 1:
    voler_a_intentar = 0
    dinero_a_retirar = int(input("Ingrese monto a retirar: $"))
    if (dinero_a_retirar > saldo_cuenta) or (dinero_a_retirar > saldo_cajero):
        print("Monto no permitido")
        voler_a_intentar = 1
    else:
        print("Dinero retirado $"+str(dinero_a_retirar))
        saldo_cuenta = saldo_cuenta - dinero_a_retirar
        saldo_cajero = saldo_cajero - dinero_a_retirar
        print("saldo cuenta="+str(saldo_cuenta))
        print("saldo cajero="+str(saldo_cajero))
    if voler_a_intentar != 1:
        retirar = str(input("Para salir ingrese una letra distinta de N: "))
        if (retirar != "N") or (saldo_cajero == 0):
            print("Hasta luego!")
            inicio = 'S'
            break
