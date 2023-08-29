#Cajero Automático
c = 0
a = True
U = int (input("Usuario: "))
while a == True:
  C = int(input("Clave: "))
  if U != 10334151:
      print("Usuario inválido")
  if U == 10334151 and C == 1803:
    n = int (input ("monto a retirar: "))
    if n > 100000 or n <= 0:
      print("monto no permitido")
    elif n <= 100000 and n > 0:
      SaldoU = 100000 - n
      SaldoC = 1000000 - n
      print("saldo cuenta=" + str(SaldoU))
      print("saldo cajero=" + str(SaldoC))
      N = input ("Desea continuar?")
      if N != "N":
        print("Gracias por operar con cajeros Mulchén")
        a = False
  if c < 3 and U == 10334151 and C != 1803:
         c += 1
         print("clave inválida")
  if c >= 3:
         print("tarjeta bloqueada")