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
      break
   if i == 3:
     print("tarjeta bloqueada")
   else:
     print("clave inválida")