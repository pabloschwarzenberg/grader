#Cajero Automático
s=20
a=40
q=40
saldo_cajero =s*20000+a*10000+q*5000
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
      a1=c//20000
      b1=c-a1*20000
      c1=b1//10000
      d1=b1-c1*10000
      e1=d1//5000
      print("billetes 20000="+str(a1))
      print("billetes 10000="+ str(c1))
      print("billetes 5000="+ str(e1))
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

    
    
    
    
    
        