#Cajero Automático
saldo_cajero = 1000000
saldo_cuenta = 100000
a = int(input())
b = int(input())
c = int(input())
n=1
n=1
while n <= 3:
  if b == 1803:
    if saldo_cuenta >= c and saldo_cajero>=c:
      saldo_cuenta=saldo_cuenta- c
      saldo_cajero=saldo_cajero-c
      print("saldo cuenta=" + str(saldo_cuenta))
      print("saldo cajero=" + str(saldo_cajero))
      break
    elif saldo_cuenta < c:
        print("monto no permitido")
    n+=1
  elif b != 1803:
      print("clave invalida")
      n += 1
if n==3:
    print("clave bloqueada")

    
    
    
    
    
  