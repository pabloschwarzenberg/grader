#Cajero Automático
usuario_luciano = 10334151
clave_del_usuario_luciano = 1803


saldogg = 100000

saldosuperlol = 1000000

CC = 1
while CC <= 3:
    usuario_del_cajero_luciano = int(input("Ingresa el Usuario, por favor estimado: "))
    clave_del_cajero_luciano= int(input("Ingresa la clave, por favor estimado: "))


    if ((usuario_del_cajero_luciano == usuario_luciano) and (clave_del_cajero_luciano == clave_del_usuario_luciano)):
      CC = 4
    else:

      print("clave invalida")
    if (CC == 3):

        print("tarjeta bloqueada")
        break
    CC = CC +1

else:
         print("100.000")
         retiro_del_money = int(input("Cuando dinero deseas retirar: "))

         if(retiro_del_money > 100000):
           print("monto excede, no es posible retirar. lo sentimos gg")
         if(retiro_del_money < 0):
           print("monto invalido, no es posible retirar. lo sentimos gg")

         else:
             if((retiro_del_money <= 100000) or (retiro_del_money == 0)):
               print()

resultado_first_luciano= saldogg - retiro_del_money
resultado_two_luciano= saldosuperlol - retiro_del_money

print("saldo cuenta=", resultado_first_luciano, "," "saldo cajero=",resultado_two_luciano) 