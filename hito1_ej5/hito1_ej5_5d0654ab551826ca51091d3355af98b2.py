#Cálculo del dígito verificador de un rut
rut=int(input())
a=rut%10
b=(rut%100)//10
c=(rut%1000)//100
d=(rut%10000)//1000
e=(rut%100000)//10000
f=(rut%1000000)//100000
g=(rut%10000000)//1000000
h=(rut%100000000)//10000000
i=(rut%1000000000)//100000000


if h==0:
  suma=a*2+b*3+c*4+d*5+e*6+f*7+g*2+h*3+i*4
  div=suma%11
  resta=11-div
  if resta==11:
    print("dv=0")
  elif resta==10:
    print("dv=k")
  else:
    print("dv=",resta)

else:
  suma=a*2+b*3+c*4+d*5+e*6+f*7+g*2+h*3+i*4
  div=suma%11
  resta=11-div
  if resta==11:
    print("dv=0")
  elif resta==10:
    print("dv=k")
  else:
    print("dv=",resta)


