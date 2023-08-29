#Cajero Automático
c = 0
bv = 20
bd = 40
bc = 40
a = True
U = int (input("Usuario: "))
if a == True:
  C = int(input("Clave: "))
  if U != 10334151:
      print("Usuario inválido")
  if U == 10334151 and C == 1803:
    n = int (input ("monto a retirar: "))
    if n > 100000 or n <= 0:
      print("monto no permitido")
    elif n <= 100000 and n > 0 and n % 5000 == 0:
      o = (n // 20000)
      print("billetes 20000=", str(o))
      p = (n % 20000) // 10000
      print("billetes 10000=", str(p))
      q = ((n % 20000) % 10000) // 5000
      print("billetes 5000=", str(q))
      SaldoU = 100000 - n
      SaldoC = 1000000 - n
      print("saldo cuenta=" + str(SaldoU))
      print("saldo cajero=" + str(SaldoC))
      N = input ("Desea continuar?")
      if N != "N":
        print("Gracias por operar con cajeros Mulchén")
        a = False
    if n <= 100000 and n > 0 and n % 5000 != 0:
      print("Solo es posible retirar múltiplos de 5.000 en este cajero")
  if c < 3 and U == 10334151 and C != 1803:
         c += 1
         print("clave inválida")
  if c >= 3:
         print("tarjeta bloqueada")
