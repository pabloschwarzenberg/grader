#Cálculo del dígito verificador de un rut
rut=int(input("rut:"))
a=(rut//10000000)
b=(rut-(a*10000000))//1000000
c=(rut-(a*10000000)-(b*1000000))//100000
d=(rut-(a*10000000)-(b*1000000)-(c*100000))//10000
e=(rut-(a*10000000)-(b*1000000)-(c*100000)-(d*10000))//1000
f=(rut-(a*10000000)-(b*1000000)-(c*100000)-(d*10000)-(e*1000))//100
g=(rut-(a*10000000)-(b*1000000)-(c*100000)-(d*10000)-(e*1000)-(f*100))//10
h=(rut-(a*10000000)-(b*1000000)-(c*100000)-(d*10000)-(e*1000)-(f*100)-(g*10))
n1=h*2+g*3+f*4+e*5+d*6+c*7+b*2+a*3
n2=11-n1%11
if n2==11:
  print("dv=0")
elif n2==10:
  print("dv=k")
else:
  print("dv=",n2)