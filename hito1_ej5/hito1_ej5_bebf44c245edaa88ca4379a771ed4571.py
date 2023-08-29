#Cálculo del dígito verificador de un rut

numero=int(input())

d1=numero//10000000
d2=(numero//1000000)%10
d3=(numero//100000)%10
d4=(numero//10000)%10
d5=(numero//1000)%10
d6=(numero//100)%10
d7=(numero//10)%10
d8=numero%10
if numero>=10000000 and numero<100000000:
  a=d8*2+d7*3+d6*4+d5*5+d4*6+d3*7+d2*2+d1*3
  c=a%11
  v=11-c
  if v==10:
    print("dv=k")
  elif v==11:
    print("dv=",0)
  else:
    print("dv=",v)
elif numero>=1000000 and numero<=10000000:
  a=d8*2+d7*3+d6*4+d5*5+d4*6+d3*7+d2*2
  c=a%11
  v=11-c
  if v==10:
    print("dv=k")
  elif v==11:
    print("dv=",0)
  else:
    print("dv=",v)
else:
  pass
