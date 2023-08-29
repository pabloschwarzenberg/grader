#Cajero Automático
usuario=int(input())
clave=int(input())
a=1000000
b=100000
i=0

while i<3:
  if usuario==10334151 and clave==1803:
    m=int(input())
    if m<=b:
      c=str(input())
      if not(c=="N"):
        b=(b-m)
        a=(a-m)
        print("saldo cuenta=",b)
        print("saldo cajero=",a)        
      else:
        break
    else:
      print("monto no permitido")  
  else:
    i=i+1
    print("clave inválida")
if i>=3:
  print("tarjeta bloqueada")