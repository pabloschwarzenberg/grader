#Cajero Automático
 saldo_cuenta=55000
saldo_cajero=955000

usuario=0

while usuario!=10334151:
    usuario=int(input("Ingrese su numero de usuario: "))
    if (usuario!=10334151):
               print("Usuario no valido: ")
    else:
               clave=int(input("Ingrese su numero de clave: "))
               if (clave!=1803):
                   print("Clave no válida, intente de nuevo")
                   clav=int(input("Ingrese su numero de clave: "))
                   if (clave!=1803):
                      print("Clave no válida, intente de nuevo: ")
                      cla=int(input("Ingrese su numero de clave: "))
                      if (cla!=1803):
                              print("Tarjeta bloqueada: ")
                      else:
                          monto_retirar=100000000000000
                          while (monto_retirar>saldo_cajero or monto_retirar>saldo_cuenta):
                              monto_retirar=int(input("Ingrese el monto a retirar: "))
                              if (monto_retirar>saldo_cajero or monto_retirar>saldo_cuenta):
                                  print("Ingrese un monto válido")
                              else:
                                  print("saldo cuenta=",saldo_cuenta-monto_retirar)
                                  print("saldo cajero=",saldo_cajero-monto_retirar)
                   else:
                              monto_retirar=1000000000
                              while (monto_retirar>saldo_cajero or monto_retirar>saldo_cuenta):
                                  monto_retirar=int(input("Ingrese el monto a retirar: "))
                                  if (monto_retirar>saldo_cuenta or monto_retirar>saldo_cajero):
                                       print("Ingrese un monto válido: ")
                                  else:
                                        print("saldo cuenta=",saldo_cuenta-monto_retirar)
                                        print("saldo cajero=",saldo_cajero-monto_retirar)
               else:
                    monto_retirar=100000000000
                    while (monto_retirar>saldo_cajero or monto_retirar>saldo_cuenta):
                                  monto_retirar=int(input("Ingrese monto a retirar: "))
                                  if (monto_retirar>saldo_cajero or monto_retirar>saldo_cuenta):
                                                    print("Ingrese un monto válido")
                                  else:
                                        print("saldo cuenta=",saldo_cuenta-monto_retirar)
                                        print("saldo cajero=",saldo_cajero-monto_retirar)    