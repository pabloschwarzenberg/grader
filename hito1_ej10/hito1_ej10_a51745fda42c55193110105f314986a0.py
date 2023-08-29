#Cajero Automático
saldocajero = 1000000
saldobanco = 100000

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

   print("[saldo cuenta=" + str(saldobanco) + "," + "saldo cajero=" + str(saldocajero)+"]")