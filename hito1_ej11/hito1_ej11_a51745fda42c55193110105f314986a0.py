#Cajero Automático
saldocajero = 1000000
saldobanco = 100000
billete20000 = 20
billete10000 = 40
billete5000 = 40


usuario = input("Ingrese usuario ")

if usuario == "10334151":
   intento = 0
   while True:
      clave = input("Ingrese clave ")
      if clave != "1803":
         intento += 1
         print("Clave Inválida")
      else:
         break

      if intento == 3:
         print("Clave Bloqueada")
         exit()

   monto = int(input("Ingrese Monto "))
   if monto > saldobanco:
      print("monto no permitido")

   saldocajero = 1000000 - monto
   saldobanco = 100000 - monto

   bil20000 = (monto // 20000)
   monto %= 20000
   bil10000 = (monto // 10000)
   monto %= 10000
   bil5000 = (monto // 5000)
   monto %= 5000

   print("[saldo cuenta=" + str(saldobanco) + "," + "saldo cajero=" + str(saldocajero)+"]")
   print("Billetes 20000="+str(bil20000))
   print("Billetes 10000="+str(bil10000))
   print("Billetes 5000="+str(bil5000))      