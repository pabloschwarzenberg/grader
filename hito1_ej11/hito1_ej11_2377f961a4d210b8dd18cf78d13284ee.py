#Cajero Automático
#Cajero Automático
for i in range(3):
   usuario = input("usuario: ")
   clave = input("clave: ")
   if usuario == "10334151" and clave == "1803":
      retiro = int(input("Retiro"))
      if retiro > 100000:
         print("monto no permitido")
      else:
         print("Saldo cuenta=", 100000 - retiro)
         print("Saldo cajero=", 1000000 - retiro)
         b20000 = min(20, retiro // 20000)
         retiro -= b20000 * 20000
         b10000 = min(40, retiro // 10000)
         retiro -= b10000 * 10000
         b5000 = min(40, retiro // 5000)
         print("billetes 20000=", b20000)
         print("billetes 10000=", b10000)
         print("billetes 5000=", b5000)
      break
   if i == 3:
     print("tarjeta bloqueada")
   else:
     print("clave inválida")



