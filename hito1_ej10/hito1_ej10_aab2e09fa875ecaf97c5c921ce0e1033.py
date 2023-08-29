#Cajero Automático
saldocajero = int(1000000)
rep = 0
if rep == 0:
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
  if usuario == 1:
    rep = 1
    break
  else:
    clave = eval(input("Clave: "))
    if clave == 1:
      rep = 1
      break
    else:
      if usuario == 10334151 and clave == 1803:
        saldo = int(100000)
        c = 1
        c2 = 1
        while c == 1:
          clave2 = eval(input("Repita clave: "))
          if clave2 == 1:
            rep = 1
            break
          if clave2 == 1803:
            break
          if c2 == 3:
            print ("tarjeta bloqueada")
            exit()
          if clave2 != 1803:
            print ("clave invalida")
            c2 = c2 + 1
        while clave2 == 1803:
          montoretiro = float(input("Cuanto quiere retirar: "))
          if montoretiro > 100000:
            print ("monto no permitido")
          if montoretiro <= 100000:
            break
        if clave == 1 or usuario == 1 or clave2 == 1:
          rep = 1
          break
        saldo = int(saldo-montoretiro)
        saldocajero = int(saldocajero-montoretiro)
        print ("saldo cuenta=",saldo)
        print ("saldo cajero=",saldocajero)