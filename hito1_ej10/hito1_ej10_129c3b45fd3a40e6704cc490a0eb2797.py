#Cajero Automático
from sys import exit
while "repetir"!="N":
  intentos_de_inicio=0
  saldo_inicial_del_cajero=1000000
  saldo_inicial_de_usuario=100000
  usuario=eval(input("indique su numero de usuario: "))
  clave=eval(input("ingrese su clave: "))
  while usuario!=10334151 and clave!=1803:
    intentos_de_inicio = intentos_de_inicio+1
    print("clave invalida")
    clave=eval(input("ingrese su clave: "))
    if intentos_de_inicio == 2:
      print("tarjeta bloqueada")
      exit()
  else:
      print("acabas de acceder a tu cuenta corriente")
      saldo_a_retirar=eval(input("indique el saldo que desea retirar: "))
      while saldo_a_retirar>100000:
        print("monto no permitido")
        saldo_a_retirar=eval(input("indique el saldo que desea retirar: "))
      else:
          saldo_nuevo_del_usuario= saldo_inicial_de_usuario-saldo_a_retirar
          saldo_nuevo_del_cajero= saldo_inicial_del_cajero-saldo_a_retirar
          print(f"saldo cuenta = ", saldo_nuevo_del_usuario)
          print(f"saldo cajero = ", saldo_nuevo_del_cajero)
          repetir=input("desea volver a realizar una transaccion: ")
          if repetir == "N":
            break      