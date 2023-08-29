#Cajero Automático
saldocajero = int(1000000)
cantidad20 = int(20)
cantidad10 = int(40)
cantidad5 = int(40)
rep = 0
saldo = int(100000) 
montoretiro = 0
if 1 == 1:
  A = 0
  B = 0
  C = 0
  D = 0
  E = 0
  F = 0
  G = 0
  H = 0
  I = 0
  J = 0
  K = 0
  L = 0
  M = 0
  N = 1
  O = 0
  P = 0
  Q = 0
  R = 0
  S = 0
  T = 0
  U = 0
  V = 0
  W = 0
  X = 0
  Y = 0
  Z = 0
while rep == 0:
  usuario = eval(input("Usuario: "))
  if usuario == 0:
    rep = 1
    break
  else:
    c = 1
    c2 = 1
    while  c == 1:
      clave = eval(input("Clave: "))
      if clave == 0:
        rep = 1
        break
      if clave == 1803:
        break
      if c2 == 3:
        print ("tarjeta bloqueada")
        break
      if clave != 1803:
        print ("clave invalida")
        c2 = c2 + 1
    if usuario == 10334151 and clave == 1803:
      while clave == 1803:
        montoretiro = int(input("Cuanto quiere retirar: "))
        if montoretiro > 100000:
          print ("monto no permitido")
        if montoretiro <= 100000:
          break
      if clave == 0 or usuario == 0 or c2 == 3:
        rep = 1
        break
      saldo = int(saldo-montoretiro)
      saldocajero = int(saldocajero-montoretiro)
      print ("saldo cuenta=",saldo)
      print ("saldo cajero=",saldocajero)
      if montoretiro >= 20000:
        op1 = int(montoretiro/20000)
        rest1 = (montoretiro-(20000*op1))
        if rest1 >= 10000:
          op2 = int(rest1/10000)
          rest2 = (rest1-(10000*op2))
          op3 = 0
          if rest2 >= 5000:
            op3 = int(rest2/5000)
        elif rest1 >= 5000:
          op3 = int(rest1/5000)
          op2 = 0
        elif rest1 == 0:
          op2=0
          op3=0
        print ("billetes 20000=",op1)
        print ("billetes 10000=",op2)
        print ("billetes 5000=",op3)
      elif montoretiro >= 10000:
        op1 = int(montoretiro/10000)
        rest1 = (montoretiro-(10000*op1))
        op2=0
        if rest1 >= 5000:
          op2 = int(rest1/5000)
        print ("billetes 20000= 0")
        print ("billetes 10000=",op1)
        print ("billetes 5000=",op2)
      elif montoretiro >= 5000:
        op1 = int(montoretiro/5000)
        print ("billetes 20000= 0")
        print ("billetes 10000= 0")
        print ("billetes 5000=",op1)
            